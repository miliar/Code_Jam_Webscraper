#include <cstdio>
#include <cstring>

const int N = 100 + 10;
const int D[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

char board[N][N];
int n, m;

bool InRange(int x, int y) {
  return 1 <= x && x <= n && 1 <= y && y <= m;
}

int main() {
  int test;
  scanf("%d", &test);
  for (int t = 1; t <= test; ++ t) {
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n; ++ i) {
      scanf("%s", board[i] + 1);
    }
    bool flag = true;
    int answer = 0;
    for (int i = 1; i <= n && flag; ++ i) {
      for (int j = 1; j <= m && flag; ++ j) {
        if (board[i][j] == '.') {
          continue;
        }
        int dx, dy;
        if (board[i][j] == '^') {
          dx = -1;
          dy = 0;
        } else if (board[i][j] == 'v') {
          dx = 1;
          dy = 0;
        } else if (board[i][j] == '<') {
          dx = 0;
          dy = -1;
        } else {
          dx = 0;
          dy = 1;
        }
        bool valid = false;
        int nx = i + dx, ny = j + dy;
        while (InRange(nx, ny)) {
          if (board[nx][ny] != '.') {
            valid = true;
            break;
          }
          nx += dx;
          ny += dy;
        }
        if (valid) {
          continue;
        }
        for (int d = 0; d < 4 && !valid; ++ d) {
          int dx = D[d][0], dy = D[d][1];
          int nx = i + dx, ny = j + dy;
          while (InRange(nx, ny)) {
            if (board[nx][ny] != '.') {
              valid = true;
              break;
            }
            nx += dx;
            ny += dy;
          }
        }
        if (valid) {
          answer ++;
        } else {
          flag = false;
          break;
        }
      }
    }
    printf("Case #%d: ", t);
    if (!flag) {
      puts("IMPOSSIBLE");
    } else {
      printf("%d\n", answer);
    }
  }
  return 0;
}
