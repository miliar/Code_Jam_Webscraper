// Google CodeJam 2013 Qualifying Round B
// dom7b5

#include <iostream>
#include <iomanip>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <memory>

using namespace std;

/* Determine if the given lawn configuration is possible. */
bool possible(int m, int n, const vector< vector<int> > &grid)
{
  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < n; ++j) {
      bool rowp = true;
      bool colp = true;
      for (int c = 0; c < n; c++) {
        if (grid[i][j] < grid[i][c]) {
          rowp = false;
          break;
        }
      }
      for (int r = 0; r < m; r++) {
        if (grid[i][j] < grid[r][j]) {
          colp = false;
          break;
        }
      }
      if (!(rowp || colp)) {
        return false;
      }
    }
  }
  return true;
}

int main(int argc, char *argv[])
{
  int ncases = 0;
  int m, n;
  cin >> ncases;
  for (int cs = 0; cs < ncases; ++cs) {
    cin >> m >> n;
    vector< vector<int> > grid(m, vector<int>(n));
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        cin >> grid[i][j];
      }
    }
    cout << "Case #" << (cs + 1) << ": "
         << (possible(m, n, grid) ? "YES" : "NO") << endl;
  }
}
