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

template<class T> ostream& operator << (ostream &o, const vector<T> &v)
{
  o << '{';
  FOREACH(it, v) o << (it == v.begin() ? "" : ", ") << *it;
  return o << '}';
}

void print(int R, int C, int r, int c, int nr, int nc) {
  vector<string> grid(R, string(C, '*'));
  //DEBUG(make_pair(R, C));
  //DEBUG(make_pair(r, c));
  //DEBUG(make_pair(nr, nc));

  for (int i = 0; i < r-1; i++)
    for (int j = 0; j < c-1; j++)
        grid[i][j] = '.';
  for (int i = 0; i < nr; i++)
    grid[i][c-1] = '.';
  for (int i = 0; i < nc; i++)
    grid[r-1][i] = '.';
  grid[0][0] = 'c';

  for (int i = 0; i < R; i++)
    cout << grid[i] << endl;
}

void run(int tc)
{
  int R, C, M;
  cin >> R >> C >> M;
  M = R*C - M;
  //DEBUG(make_pair(make_pair(R, C), M));

  cout << "Case #" << (tc + 1) << ":" << endl;
  for (int i = 0; i < R; i++)
    for (int j = 0; j < C; j++) {
      int m = (i+1) * (j+1);
      if (m < M) continue;
      if (m == M && (R == 1 || C == 1 || M == 1 || (i > 0 && j > 0))) {
        print(R, C, i+1, j+1, i+1, j+1);
        return;
      }
      if (m > M && i > 1 && j > 1 && m - M <= i - 1 + j - 2) {
        int mines = m - M;
        int spaces = i + j + 1 - mines;
        int nr =  max(i + 1 - mines, 2);
        int nc =  spaces - nr;
        print (R, C, i+1, j+1, nr, nc);
        return;
      }
    }
  cout << "Impossible" << endl;
}

int main()
{
  int T = 0, tc = 0;
  for (cin >> T; tc < T; tc++) run(tc);
  return 0;
}
