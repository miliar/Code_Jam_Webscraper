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

bool isgood(int64 r, const vector<int64> &m) {
  if (r < 0)
    return false;
  for (int i = 1; i < m.size(); i++)
    if (m[i-1] - r > m[i])
      return false;
  return true;
}

int64 numeat(int64 r, const vector<int64> &m) {
  int64 num = 0;
  for (int i = 0; i < m.size() - 1; i++)
    num += min(r, m[i]);
  return num;
}

void run(int tc)
{
  int N;
  cin >> N;
  vector<int64> m(N);
  for (int i = 0; i < N; i++)
    cin >> m[i];

  int64 res1 = 0;
  for (int i = 1; i < N; i++)
    res1 += max(m[i-1] - m[i], 0ll);

  int64 good = 0, bad = -1;
  for (int i = 0; i < N; i++)
    good = max(m[i], good);

  while (good-bad > 1) {
    int64 mid = (bad + good) / 2;
    if (isgood(mid, m)) good = mid;
    else                bad = mid;
  }
  int64 res2 = numeat(good, m);

  cout << "Case #" << (tc + 1) << ": " << res1 << " " << res2 << endl;
}

int main()
{
  int T = 0, tc = 0;
  for (cin >> T; tc < T; tc++) run(tc);
  return 0;
}
