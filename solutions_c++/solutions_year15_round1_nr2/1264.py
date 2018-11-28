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
  int B, N;
  cin >> B >> N;
  vector<int> M(B);
  for (int i = 0; i < B; i++)
    cin >> M[i];

  map<vector<int>, int> state_map;
  vector<int> b, state(B);
  state[0] = M[0];
  b.push_back(1);
  while (b.size() < N) {
    int mni = 0, mn = state[0];
    for (int i = 1; i < B; i++) {
      if (state[i] < mn) {
        mn = state[i];
        mni = i;
      }
    }

    for (int i = 0; i < B; i++)
      state[i] -= mn;
    state[mni] = M[mni];
    if (state_map.find(state) != state_map.end())
      break;

    state_map[state] = b.size();
    b.push_back(mni + 1);
  }

  int res;
  if (b.size() == N) {
    res = b[N-1];
  } else {
    int cycle = state_map[state];
    int orbit = b.size() - cycle;
    int pos = cycle + ((N - cycle - 1) % orbit);
    res = b[pos];
  }

  cout << "Case #" << (tc + 1) << ": " << res << endl;
}

int main()
{
  int T = 0, tc = 0;
  for (cin >> T; tc < T; tc++) run(tc);
  return 0;
}
