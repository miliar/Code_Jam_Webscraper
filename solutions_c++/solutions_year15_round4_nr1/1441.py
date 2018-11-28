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
  int R, C;
  cin >> R >> C;
  vector<string> grid(R);
  for (int i = 0; i < R; i++)
    cin >> grid[i];

  int dy[4] = { 0, 1, 0, -1 };
  int dx[4] = { 1, 0, -1, 0 };
  int res = 0;
  for (int i = 0; i < R; i++)
    for (int j = 0; j < C; j++)
      if (grid[i][j] != '.') {
        int d = -1;
        bool found = false;
        if (grid[i][j] == '>') d = 0;
        if (grid[i][j] == 'v') d = 1;
        if (grid[i][j] == '<') d = 2;
        if (grid[i][j] == '^') d = 3;

        for (int k = 0; k < 4 && !found; k++) {
          int ci = i + dy[d], cj = j + dx[d];
          while (ci >= 0 && ci < R && cj >= 0 && cj < C) {
            if (grid[ci][cj] != '.') {
              if (k != 0) res++;
              found = true;
              break;
            }
            ci += dy[d];
            cj += dx[d];
          }
          d = (d + 1) % 4;
        }

        if (!found) {
          cout << "Case #" << (tc + 1) << ": IMPOSSIBLE" << endl;
          return;
        }
      }
  cout << "Case #" << (tc + 1) << ": " << res << endl;
}

int main()
{
  int T = 0, tc = 0;
  for (cin >> T; tc < T; tc++) run(tc);
  return 0;
}
