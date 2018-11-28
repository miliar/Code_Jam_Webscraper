#include "cstdio"
#include "iostream"
#include "algorithm"
#include "vector"
#include "string"
#include "map"

using namespace std;

vector<string> grid;

vector<int> rcount;
vector<int> ccount;

bool impossible_check(int r, int c) {
  for (int i = 0; i < r; i++)  {
    for (int j = 0; j < c; j++) {
      if ( grid[i][j] != '.' ) {
        if ( rcount[i] == 1 && ccount[j] == 1 ) {
          return true;
        }
      }
    }
  }

  return false;
}

int main() {
  int ntc;

  cin >> ntc;
  for (int tc = 1; tc <= ntc; tc++) {
    int r, c;
    cin >> r >> c;

    rcount.assign(r, 0);
    ccount.assign(c, 0);

    grid.assign( r, "" );
    int sumall = 0;
    for (int i = 0; i < r; i++) {
      cin >> grid[i];
      for (int j = 0; j < c; j++) {
        if ( grid[i][j] != '.' ) {
          rcount[i]++;
          ccount[j]++;
          sumall++;
        }
      }
    }

    if ( sumall == 0 ) {
      printf("Case #%d: 0\n", tc);
    } else if ( impossible_check(r, c) ) {
      printf("Case #%d: IMPOSSIBLE\n", tc);
    } else {
      vector<string> ngrid(r, string(c, '.'));

      int ans = 0;
      for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
          if ( grid[i][j] != '.' ) {
            if ( ngrid[i][j] == '.' && grid[i][j] == '<' ) {
              ans++;
              ngrid[i][j] = 'X';
            }
            break;
          }
        }

        for (int j = c - 1; j >= 0; j--) {
          if ( grid[i][j] != '.' ) {
            if ( ngrid[i][j] == '.' && grid[i][j] == '>' ) {
              ans++;
              ngrid[i][j] = 'X';
            }
            break;
          }
        }
      }

      for (int j = 0; j < c; j++) {
        for (int i = 0; i < r; i++) {
          if ( grid[i][j] != '.' ) {
            if ( ngrid[i][j] == '.' && grid[i][j] == '^' ) {
              ans++;
              ngrid[i][j] = 'X';
            }
            break;
          }
        }

        for (int i = r - 1; i >= 0; i--) {
          if ( grid[i][j] != '.' ) {
            if ( ngrid[i][j] == '.' && grid[i][j] == 'v' ) {
              ans++;
              ngrid[i][j] = 'X';
            }
            break;
          }
        }
      }

      printf("Case #%d: %d\n", tc, ans);
    }
  }

  return 0;
}
