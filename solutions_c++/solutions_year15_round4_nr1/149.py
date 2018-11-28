#define NDEBUG
#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;


void solve() {
  int R, C;
  cin >> R >> C;
  char mat[101][101];
  for (int i=0; i<R; ++i) {
    cin >> mat[i];
  }
  int ans = 0;
  for (int y=0; y<R; ++y) {
    for (int x=0; x<C; ++x) {
      if (mat[y][x] == '.') {
        continue;
      }
      const int dy[] = {-1, 0, 1, 0};
      const int dx[] = {0, 1, 0, -1};
      const char* arrows = "^>v<";
      bool outcomes[4];
      bool any = false;
      for (int dir=0; dir<4; ++dir) {
        int ny = y, nx = x;
        while (1) {
          ny += dy[dir]; nx += dx[dir];
          if (ny < 0 || ny >= R || nx < 0 || nx >= C) {
            outcomes[dir] = false;
            break;
          }
          if (mat[ny][nx] != '.') {
            outcomes[dir] = true;
            any = true;
            break;
          }
        }
      }
      int me = strchr(arrows, mat[y][x]) - arrows;
      if (!outcomes[me]) {
        if (any) {
          ++ans;
        } else {
          printf("IMPOSSIBLE\n");
          return;
        }
      }
    }
  }

  printf("%d\n", ans);
}

int main() {
  ios_base::sync_with_stdio(0);

  int T;
  cin >> T;
  for (int tt=1; tt<=T; ++tt) {
    printf("Case #%d: ", tt);
    solve();
    fflush(stdout);
  }
}
