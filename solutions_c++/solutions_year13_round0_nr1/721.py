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

bool winner(const vector<string> &grid, char player) {
  int dir[][4] = {
    {0, 0, 1, 0}, {0, 1, 1, 0}, {0, 2, 1, 0}, {0, 3, 1, 0},
    {0, 0, 0, 1}, {1, 0, 0, 1}, {2, 0, 0, 1}, {3, 0, 0, 1},
    {0, 0, 1, 1}, {0, 3, 1, -1}
  };
  for (int i = 0; i < sizeof(dir) / sizeof(dir[0]); i++) {
    int cnt = 0, sr = dir[i][0], sc = dir[i][1];
    for (int j = 0; j < 4; j++) {
      char val = grid[sr + dir[i][2]*j][sc + dir[i][3]*j];
      if (val == player || val == 'T')
        cnt++;
    }
    if (cnt == 4)
      return true;
  }
  return false;
}

void run(int tc)
{
  vector<string> grid(4);
  bool hasdot = false;
  for (int i = 0; i < 4; i++) {
    cin >> grid[i];
    if (grid[i].find('.', 0) != string::npos)
      hasdot = true;
  }

  string out;
  if (winner(grid, 'X'))
    out = "X won";
  else if (winner(grid, 'O'))
    out = "O won";
  else if (hasdot)
    out = "Game has not completed";
  else
    out = "Draw";

  cout << "Case #" << (tc + 1) << ": " << out << endl;
}

int main()
{
  int T = 0, tc = 0;
  for (cin >> T; tc < T; tc++) run(tc);
  return 0;
}
