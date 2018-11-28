#include <iostream>
#include <cstdio>

using namespace std;

int main(int argc, char **argv)
{
  int before[4][4], after[4][4];
  int num_round;

  cin >> num_round;
  for (int i = 0; i < num_round; ++i) {
    int before_row, after_row;
    cin >> before_row;
    --before_row;
    for (int m = 0; m < 4; ++m) {
      for (int n = 0; n < 4; ++n) {
        cin >> before[m][n];
      }
    }
    cin >> after_row;
    --after_row;
    for (int m = 0; m < 4; ++m) {
      for (int n = 0; n < 4; ++n) {
        cin >> after[m][n];
      }
    }

    int common_count = 0;
    int num;
    for (int m = 0; m <  4; ++m) {
      for (int n = 0; n < 4; ++n) {
        if (before[before_row][m] == after[after_row][n]) {
          ++common_count;
          num = before[before_row][m];
        }
      }
    }
    cout << "Case #" << i + 1 << ": ";
    if (common_count == 1) {
      cout << num << endl;
    } else if (common_count == 0) {
      cout << "Volunteer cheated!" << endl;
    } else {
      cout << "Bad magician!" << endl;
    }
  }

  return 0;
}
