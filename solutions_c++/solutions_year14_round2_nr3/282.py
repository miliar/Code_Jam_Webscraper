#include <algorithm>
#include <cmath>
#include <climits>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <tuple>
using namespace std;

typedef long long int64;
//typedef __int128_t int128;
typedef vector<int> veci;
typedef vector<string> vecs;

#define VAR(a, b) __typeof(b) a=(b)
#define FOREACH(it, c) for (VAR(it, (c).begin()); it != (c).end(); ++it)
#define TRACE(x) cout << #x << endl
#define DEBUG(x) cout << #x " = " << (x) << endl
#define DEBUGA(a, n) VAR(__p, a); cout << #a " = {"; for (int __i = 0; __i < n; ++__i, ++__p) cout << (__i == 0 ? "" : ", ") << *(__p); cout << "}" << endl
#define CLR(a, val) memset(a, val, sizeof(a))

template<class T1, class T2> ostream& operator << (ostream &o, const pair<T1, T2> &p)
{
  return o << "(" << p.first << ", " << p.second << ")";
}

template<class T1, class T2, class T3> ostream& operator << (ostream &o, const tuple<T1, T2, T3> &t)
{
  return o << "(" << get<0>(t) << ", " << get<1>(t) << ", " << get<2>(t) << ")";
}

template<class T1, class T2, class T3, class T4> ostream& operator << (ostream &o, const tuple<T1, T2, T3, T4> &t)
{
  return o << "(" << get<0>(t) << ", " << get<1>(t) << ", " << get<2>(t) << ", " << get<3>(t) << ")";
}

template<class T> ostream& operator << (ostream &o, const vector<T> &v)
{
  o << '{';
  FOREACH(it, v) o << (it == v.begin() ? "" : ", ") << *it;
  return o << '}';
}

vector<int> best;

void search(
    const vector<veci> &G,
    vector<int> &path,
    vector<int> &uniq,
    vector<int> &outb) {
  int N = G.size();
  if (path.size() == 2*N-1) {
    if (best.size() == 0 || uniq < best) {
      best = uniq;
    }
    return;
  }
  if (best.size() && uniq > best)
    return;

  int curr = path.back();
  for (auto next : G[curr]) {
    if (outb[next] == -1) {
      outb[next] = curr;
      path.push_back(next);
      uniq.push_back(next);
      search(G, path, uniq, outb);
      uniq.pop_back();
      path.pop_back();
      outb[next] = -1;
    }
  }
  if (outb[curr] >= 0) {
    int ret = outb[curr];
    outb[curr] = -2;
    path.push_back(ret);
    search(G, path, uniq, outb);
    path.pop_back();
    outb[curr] = ret;
  }
}

void run(int tc)
{
  int N, M;
  cin >> N >> M;

  vector<string> zips(N);
  map<int, string> zipmap;
  for (int i = 0; i < N; i++) {
    cin >> zips[i];
    zipmap[i] = zips[i];
  }

  sort(zips.begin(), zips.end());
  map<string, int> posmap;
  for (int i = 0; i < N; i++)
    posmap[zips[i]] = i;

  vector<veci> G(N);
  for (int i = 0; i < M; i++) {
    int x, y;
    cin >> x >> y;
    x = posmap[zipmap[x-1]];
    y = posmap[zipmap[y-1]];
    G[x].push_back(y);
    G[y].push_back(x);
  }

  cout << "Case #" << (tc + 1) << ": ";

  best.clear();
  for (int i = 0; i < N; i++) {
    vector<int> path = { i };
    vector<int> uniq = { i };
    vector<int> outb(N, -1);
    outb[i] = -2;
    search(G, path, uniq, outb);
  }
  for (auto p : best)
    cout << zips[p];
  cout << endl;
}

int main()
{
  int T = 0, tc = 0;
  for (cin >> T; tc < T; tc++) run(tc);
  return 0;
}
