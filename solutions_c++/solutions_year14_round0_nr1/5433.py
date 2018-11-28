#include <iostream>

using namespace std;

int main()
{
  int T;

  cin >> T;

  for (int cas = 1; cas <= T; cas++) {
    int row[2];
    int table[2][4][4];
    
    for (int i = 0; i < 2; i++) {
      cin >> row[i];
      for (int j = 0; j < 4; j++) {
        for (int k = 0; k < 4; k++) {
          cin >> table[i][j][k];
        }
      }
    }

    int n = 0;
    int ans = 0;

    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
        if (table[0][row[0]-1][i] == table[1][row[1]-1][j]) {
          ans = table[0][row[0]-1][i];
          n++;
        }
      }
    }
    cout << "Case #" << cas << ": ";
    if (n == 0) {
      cout << "Volunteer cheated!";
    } else if (n == 1) {
      cout << ans;
    } else {
      cout << "Bad magician!";
    }
    cout << endl;
  }

  return 0;
}
