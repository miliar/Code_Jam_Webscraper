#include <iostream>
#include <iomanip>
using namespace std;

string s[100];
const int dx[4] = {-1,1,0,0};
const int dy[4] = {0,0,-1,1};
//                 ^  v < >

int main() {
  ios::sync_with_stdio(0);
  int t; cin >> t;
  for (int T = 1; T <= t; T++) {
    cout << "Case #" << T << ": ";
    int r, c;
    cin >> r >> c;
    for (int i = 0; i < r; i++)
      cin >> s[i];
    int a = 0;
    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
        if (s[i][j] == '.')
          continue;
        int v = 0;
        bool q = false;
        for (int k = 0; k < 4; k++) {
          int x = i, y = j;
          while (true) {
            x += dx[k]; y += dy[k];
            if (x < 0 || x == r || y < 0 || y == c) {
              v++;
              if ((k == 0 && s[i][j] == '^') ||
                  (k == 1 && s[i][j] == 'v') ||
                  (k == 2 && s[i][j] == '<') || 
                  (k == 3 && s[i][j] == '>'))
                q = true;
              break;
            }
            if (s[x][y] != '.')
              break;
          }
        }
        //cout << i << " " << j << " " << v << " " << q << endl;
        if (v == 4) {
          cout << "IMPOSSIBLE";
          goto VELOCIRAPTOR;
        }
        if (v && q)
          a++;
      }
    }
    cout << a;
    VELOCIRAPTOR:
    cout << "\n";
  }
  return 0;
}
