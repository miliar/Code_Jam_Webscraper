#include <iostream>
#include <vector>

using namespace std;

int row[2][4];
int result[4];

int main()
{
  int ntc;  cin >> ntc;
  for (int tc = 1; tc <= ntc; ++tc) {
    int aux;
    for (int r = 0; r < 2; ++r) {
      int k; cin >> k; --k;
      for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
          if (i == k) cin >> row[r][j];
          else cin >> aux;
        }
      }
    }
    int n = 0;
    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) if (row[0][i] == row[1][j]) {
        result[n++] = row[0][i];
        break;
      }
    }
    cout << "Case #" << tc << ": ";
    if (n == 0) cout << "Volunteer cheated!";
    else if (n > 1) cout << "Bad magician!";
    else cout << result[0];
    cout << endl;
  }
}
