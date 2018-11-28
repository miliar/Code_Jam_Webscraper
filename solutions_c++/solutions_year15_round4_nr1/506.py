#include <iostream>
using namespace std;

int dir[4][2] = {1, 0, -1, 0, 0, 1, 0, -1};
int map[100][100];

int main() {
  cin.sync_with_stdio(false);
  cin.tie(NULL); cout.tie(NULL);
  int T;
  cin >> T;
  for (int cas = 1; cas <= T; cas++) {
    int R, C;
    cin >> R >> C;
    for (int i = 0; i < R; i++) {
      for (int j = 0; j < C; j++) {
        char dir;
        cin >> dir;
        if (dir == 'v') {
          map[i][j] = 0;
        } else if (dir == '^') {
          map[i][j] = 1;
        } else if (dir == '>') {
          map[i][j] = 2;
        } else if (dir == '<') {
          map[i][j] = 3;
        } else {
          map[i][j] = -1;
        }
      }
    }
    int counts = 0;
    cout << "Case #" << cas << ": ";
    for (int i = 0; counts >= 0 && i < R; i++) {
      for (int j = 0; counts >= 0 && j < C; j++) {
        //cout << i << " " << j << endl;
        if (map[i][j] == -1) continue;
        int olddir = map[i][j];
        int tempx = i + dir[olddir][0], tempy = j + dir[olddir][1];
        while (tempx >= 0 && tempx < R && tempy >= 0 && tempy < C && map[tempx][tempy] == -1) {
          tempx += dir[olddir][0];
          tempy += dir[olddir][1];
        }
        if (tempx >= 0 && tempx < R && tempy >= 0 && tempy < C) {
          //cout << "OK" << endl;
          continue;
        }
        bool canchange = false;
        for (int k = 0; k < 4; k++) {
          if (k == olddir) continue;
          int tempx = i + dir[k][0], tempy = j + dir[k][1];
          while (tempx >= 0 && tempx < R && tempy >= 0 && tempy < C && map[tempx][tempy] == -1) {
            tempx += dir[k][0];
            tempy += dir[k][1];
          }
          if (tempx >= 0 && tempx < R && tempy >= 0 && tempy < C) {
            canchange = true;
            break;
          }
        }
        if (canchange) {
          counts++;
        } else {
          counts = -1;
          break;
        }
      }
    }
    if (counts == -1) {
      cout << "IMPOSSIBLE" << endl;
    } else {
      cout << counts << endl;
    }
  }
}
