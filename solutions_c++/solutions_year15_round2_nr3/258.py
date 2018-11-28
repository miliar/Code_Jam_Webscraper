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

void run(int tc)
{
  int64 N;
  cin >> N;
  vector<pair<int64, int64>> h;
  for (int64 i = 0; i < N; i++) {
    int64 D, H, M;
    cin >> D >> H >> M;
    for (int64 i = 0; i < H; i++) {
      h.push_back(make_pair(D, M + i));
    }
  }
  sort(h.begin(), h.end());

  cout << "Case #" << (tc + 1) << ": ";
  if (h.size() <= 1) {
    cout << 0 << endl;
    return;
  }
  int64 t1 = (360-h[0].first) * h[0].second;
  int64 t2 = (360-h[1].first) * h[1].second;
  if (t1 < t2) {
    int64 t3 = t1 + 360 * h[0].second;
    if (t3 <= t2)
      cout << 1 << endl;
    else
      cout << 0 << endl;
  } else {
    int64 t3 = t2 + 360 * h[1].second;
    if (t3 <= t1)
      cout << 1 << endl;
    else
      cout << 0 << endl;
  }
}

int main()
{
  int T = 0, tc = 0;
  for (cin >> T; tc < T; tc++) run(tc);
  return 0;
}
