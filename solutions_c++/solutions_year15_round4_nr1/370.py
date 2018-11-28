#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

int dr[] = {-1, 0, 1, 0};
int dc[] = {0, -1, 0, 1};

int R, C;
string A[110];
bool vis[110][110][4];

int main() {
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    cin >> R >> C;
    for (int i = 0; i < R; i++) {
      cin >> A[i];
    }

    int result = 0;
    bool impos = false;
    for (int i = 0; i < R; i++) {
      for (int j = 0; j < C; j++) {
        if (A[i][j] == '.') continue;

        int dir;
        switch(A[i][j]) {
          case '^': dir = 0; break;
          case '<': dir = 1; break;
          case 'v': dir = 2; break;
          default: dir = 3; break;
        }
        int m = 0;
        for (int ed = 0; ed < 4; ed++) {
          for (int k = 1; ; k++) {
            int r = i + k * dr[ed];
            int c = j + k * dc[ed];
            if (r < 0 || R <= r || c < 0 || C <= c) {
              break;
            }
            if (A[r][c] != '.') {
              m |= 1 << ed;
              break;
            }
          }
        }
        if (!m) {
          impos = true;
        } else if (~m & 1 << dir) {
          result++;
        }
      }
    }
    cout << "Case #" << t << ": ";
    if (impos) {
      cout << "IMPOSSIBLE\n";
    } else {
      cout << result << endl;
    }
  }
  return 0;
}
