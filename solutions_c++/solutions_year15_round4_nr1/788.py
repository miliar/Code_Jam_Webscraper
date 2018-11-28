#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
  int T;
  cin >> T;
  for (int cas = 1; cas <= T; cas++) {
    int R, C;
    cin >> R >> C;
    vector<string> m;
    for (int i = 0; i < R; i++) {
      string s;
      cin >> s;
      m.push_back(s);
    }
    bool u[101][101];
    for (int r = 0; r < R; r++) {
      for (int c = 0; c < C; c++) {
        u[r][c] = false;
      }
    }
    
    bool imp = false;
    int n = 0;

    for (int r = 0; r < R; r++) {
      for (int c = 0; c < C; c++) {
        if (m[r][c] == '.') continue;
        bool dame = true;
        bool change = true;
        for (int r2 = 0; r2 < r; r2++) {
          if (m[r2][c] != '.') {
            dame = false;
            if (m[r][c] == '^') change = false;
          }
        }
        for (int r2 = r + 1; r2 < R; r2++) {
          if (m[r2][c] != '.') {
            dame = false;
            if (m[r][c] == 'v') change = false;
          }
        }
        for (int c2 = 0; c2 < c; c2++) {
          if (m[r][c2] != '.') {
            dame = false;
            if (m[r][c] == '<') change = false;
          }
        }
        for (int c2 = c + 1; c2 < C; c2++) {
          if (m[r][c2] != '.') {
            dame = false;
            if (m[r][c] == '>') change = false;
          }
        }
        if (dame) {
          imp = true;
          break;
        }
        if (change) n++;
      }
    }
    cout << "Case #" << cas << ": ";
    if (imp) {
      cout << "IMPOSSIBLE";
    } else {
      cout << n;
    }
    cout << endl;
  }

  return 0;
}
