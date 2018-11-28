#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

int R, C, M;
bool mine[5][5];
bool vis[5][5];

void dfs(int y, int x) {
  if(vis[y][x]) return;
  vis[y][x] = true;

  bool find_mine = false;
  for(int dx = -1; dx <= 1; dx++) {
    for(int dy = -1; dy <= 1; dy++) {
      int ny = y + dy;
      int nx = x + dx;
      if(0 <= ny && ny < R && 0 <= nx && nx < C) {
        if(mine[ny][nx]) find_mine = true;
      }
    }
  }

  if(find_mine == false) {
    for(int dx = -1; dx <= 1; dx++) {
      for(int dy = -1; dy <= 1; dy++) {
        int ny = y + dy;
        int nx = x + dx;
        if(0 <= ny && ny < R && 0 <= nx && nx < C) {
          dfs(ny, nx);
        }
      }
    }
  }
}

int main() {
  int T; cin >> T;
  for(int t = 1; t <= T; ++t) {
    cin >> R >> C >> M;
    int comb = (1 << M) - 1;

    bool find_answer = false;
    int ans_y, ans_x;
    while(comb < 1 << (R*C)) {
      for(int i = 0; i < R; i++) {
        for(int j = 0; j < C; j++) {
          if((comb >> (C*i+j)) & 1) mine[i][j] = true;
          else mine[i][j] = false;
        }
      }

      for(int i = 0; i < R; i++) {
        for(int j = 0; j < C; j++) {
          memset(vis, 0, sizeof(vis));
          dfs(i, j);
          bool ok = true;
          for(int y = 0; y < R; y++) {
            for(int x = 0; x < C; x++) {
              if(mine[y][x] == false && vis[y][x] == false) ok = false;
            }
          }
          if(ok) {
            find_answer = true;
            ans_y = i, ans_x = j;
            goto exit;
          }
        }
      }

      int x = comb & -comb, y = comb + x;
      comb = ((comb & ~y) / x >> 1) | y;
    }
exit:
    cout << "Case #" << t << ":" << endl;
    if(find_answer) {
      for(int y = 0; y < R; y++) {
        for(int x = 0; x < C; x++) {
          if(y == ans_y && x == ans_x) {
            cout << 'c';
          }
          else if(mine[y][x]) {
            cout << '*';
          }
          else {
            cout << '.';
          }
        }
        cout << endl;
      }
    }
    else {
      cout << "Impossible" << endl;
    }
  }
}
