// mars.ma
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;


int main(void)
{
  int testcase;
  cin >> testcase;
  for (int tc = 1; tc <= testcase; tc++) {
    int row, col, mine;
    cin >> row >> col >> mine;
    int width = col;
    int height = row;
    cout << "Case #" << tc << ":\n";

    int blank = row*col - mine;
    row = min(width, height);
    col = max(width, height);
    vector<string> config(row, string(col, '.'));
    bool possible = true;
    if (1 == blank) {
      config = vector<string>(row, string(col, '*'));
      config[0][0] = '.';
    } else if (1 == min(row, col)) {
      for (int m = 0; m < mine; ++m) {
        config[0][col-m-1] = '*';
      }
    } else if (2 == min(row, col)) {
      if (((1 != blank) && (mine%2)) || (2 == blank)) {
        possible = false;
      } else {
        for (int m = 0; m < mine; ++m) {
          config[(m+1)%2][col - m/2 - 1] = '*';
        }
      }
    } else {
      if ((2 == blank) || (3 == blank) || (5 == blank) || (7 == blank)) {
        possible = false;
      } else if (4 == blank) {
        config = vector<string>(row, string(col, '*'));
        for (int r = 0; r < 2; ++r) {
          for (int c = 0; c < 2; ++c) {
            config[r][c] = '.';
          }
        }
      } else if (6 == blank) {
        config = vector<string>(row, string(col, '*'));
        for (int r = 0; r < 2; ++r) {
          for (int c = 0; c < 3; ++c) {
            config[r][c] = '.';
          }
        }
      } else if (8 == blank) {
        config = vector<string>(row, string(col, '*'));
        for (int r = 0; r < 3; ++r) {
          for (int c = 0; c < 3; ++c) {
            config[r][c] = '.';
          }
        }
        config[2][2] = '*';
      } else if (9 == blank) {
        config = vector<string>(row, string(col, '*'));
        for (int r = 0; r < 3; ++r) {
          for (int c = 0; c < 3; ++c) {
            config[r][c] = '.';
          }
        }
      } else {
        int pad = mine/row;
        for (int c = 0; c < min(pad, col-3); ++c) {
          for (int r = 0; r < row; ++r) {
            config[r][col-c-1] = '*';
          }
        }

        if (pad < col-3) {
          int remain = mine%row;
          for (int r = 0; r < min(remain, row-2); ++r) {
            config[row-r-1][col-1-pad] = '*';
          }

          if (remain+1 == row) {
            config[row-1][col-2-pad] = '*';
          }
        } else {
          int remain = mine - row*(col-3);
          if (blank%2) {
            for (int m = 0; (m < (row-3)) && (0 < remain); ++m, --remain) {
              config[row-m-1][2] = '*';
            }
          } else {
            for (int m = 0; (m < (row-2)) && (0 < remain); ++m, --remain) {
              config[row-m-1][2] = '*';
            }
          }

          for (int m = 0; m < remain; ++m) {
            config[row-m/2-1][(m+1)%2] = '*';
          }
        }
      }
    }

    if (possible) {
      // print the config
      config[0][0] = 'c';
      for (int r = 0; r < height; ++r) {
        if (height < width) {
          cout << config[r] << endl;
        } else {
          for (int c = 0; c < width; ++c) {
            cout << config[c][r];
          }
          cout << endl;
        }
      }
    } else {
      cout << "Impossible\n";
    }
  }

  return 0;
}

