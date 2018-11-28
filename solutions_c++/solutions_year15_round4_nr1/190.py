#include <bits/stdc++.h>
#include <boost/range/irange.hpp>
using namespace std;
using boost::irange;

using real_int = int;
#define int int64_t

tuple<int, int> dir(char c) {
  switch (c) {
  case '>': return make_tuple( 0,  1);
  case '<': return make_tuple( 0, -1);
  case '^': return make_tuple(-1,  0);
  case 'v': return make_tuple( 1,  0);
  default: assert(false);
  }
}

bool walks_off(vector<string> const& grid, int y, int x, int dy, int dx) {
  for (y += dy, x += dx; 0<=y && y<(int)grid.size() &&
                         0<=x && x<(int)grid[y].size();
       y += dy, x += dx)
    if (grid[y][x] != '.')
      return false;
  return true;
}

int solve() {
  int r, c; cin >> r >> c;
  vector<string> grid;
  copy_n(istream_iterator<string>(cin), r, back_inserter(grid));
  int changes=0;
  for (int i : irange<int>(0, r)) {
    for (int j : irange<int>(0, c)) {
      if (grid[i][j] != '.') {
        int dy, dx;
        tie(dy, dx) = dir(grid[i][j]);
        if (!walks_off(grid, i, j, dy, dx))
          continue;
        ++changes;
        bool ok=false;
        for (char c : {'<', '>', 'v', '^'}) {
          grid[i][j] = c;
          tie(dy, dx) = dir(c);
          if (!walks_off(grid, i, j, dy, dx)) {
            ok=true;
            break;
          }
        }
        if (!ok)
          return -1;
      }
    }
  }
  return changes;
}

real_int main() {
  int testcases; cin >> testcases;
  for (auto i : irange<int>(1, testcases+1)) {;
    cout << "Case #" << i << ": ";
    int x=solve();
    if (x==-1)
      cout << "IMPOSSIBLE";
    else
      cout << x;
    cout << '\n';
  }
}

/*
 * Local variables:
 * compile-command:"g++ -D_GLIBCXX_DEBUG -g3 -ggdb3 -O0 -Wall -Wextra -std=c++14 pegman.cc -o pegman && for f in *.in; do echo \"--- $f -------------\"; ./pegman <$f; done"
 * end:
 */

