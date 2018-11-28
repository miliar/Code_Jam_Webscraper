#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>

typedef long long ll;
typedef unsigned int ui;

using namespace std;

char grid[102][102];
char dr[] = {0, -1, 0, 1, 0};
char dc[] = {0, 0, 1, 0, -1};
int R, C;

int readChar() {
  for (;;) {
    int c = getchar();
    if (c == '.') return 0;
    if (c == '^') return 1;
    if (c == '>') return 2;
    if (c == 'v') return 3;
    if (c == '<') return 4;
  }
}

int go(int r, int c, int d) {
  do {
    r += dr[d];
    c += dc[d];
  } while (grid[r][c] == 0 && r > 0 && c > 0 && r <= R && c <= C);
  return grid[r][c];
}

void solve() {
  int res = 0;

  memset(grid, 0, sizeof(grid));
  
  scanf("%d%d\n", &R, &C);
  for (int r = 1; r <= R; r++)
    for (int c = 1; c <= C; c++)
      grid[r][c] = readChar();

  for (int r = 1; r <= R; r++)
    for (int c = 1; c <= C; c++) {
      int d = grid[r][c];
      if (d == 0) continue;
      if (go(r, c, d) != 0) continue;
      if (go(r, c, 1) || go(r, c, 2) || go(r, c, 3) || go(r, c, 4))
        res++;
      else {
        puts("IMPOSSIBLE");
        return;
      }
    }

  printf("%d\n", res);
}

int main() {
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    printf("Case #%d: ", t);
    solve();
  }
  return 0;
}
