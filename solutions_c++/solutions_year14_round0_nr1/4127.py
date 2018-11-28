#include <iostream>

using namespace std;

int main(int argc, char** argv) {
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    int a1;
    cin >> a1;
    int grid1[4][4];
    for (int j = 0; j < 4; ++j) {
      for (int k = 0; k < 4; ++k) {
        cin >> grid1[j][k];
      }
    }
    int a2;
    cin >> a2;
    int grid2[4][4];
    for (int j = 0; j < 4; ++j) {
      for (int k = 0; k < 4; ++k) {
        cin >> grid2[j][k];
      }
    }
    int possible = -1;
    int num_possible = 0;
    for (int j = 0; j < 4; ++j) {
      for (int k = 0; k < 4; ++k) {
        if (grid1[a1 - 1][j] == grid2[a2 - 1][k]) {
          num_possible++;
          possible = grid1[a1 - 1][j];
        }
      }
    }
    if (num_possible == 0) {
     cout << "Case #" << i << ": Volunteer cheated!" << endl;
    }
    if (num_possible > 1) {
      cout << "Case #" << i << ": Bad magician!" << endl;
    }
    if (num_possible == 1) {
      cout << "Case #" << i << ": " << possible << endl;
    }
  }
  return 0;
}
