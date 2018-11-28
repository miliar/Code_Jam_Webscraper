#include <cstdio>

int main() {
  int T;
  scanf("%d", &T);
  for (int tc = 1; tc <= T; tc++) {
    int W, H;
    char grid[111][111];
    int rowcount[111], colcount[111];

    scanf("%d %d", &H, &W);
    for (int y = 0; y < H; y++) for (int x = 0; x < W; x++) scanf(" %c", &grid[y][x]);
    for (int y = 0; y < H; y++) for (int x = 0; x < W; x++) rowcount[y] = colcount[x] = 0;
    for (int y = 0; y < H; y++) for (int x = 0; x < W; x++) if (grid[y][x] != '.') {
      rowcount[y]++;
      colcount[x]++;
    }

    bool impossible = false;

    for (int y = 0; y < H; y++) for (int x = 0; x < W; x++) if (grid[y][x] != '.') {
      if (rowcount[y] == 1 && colcount[x] == 1) impossible = true;
    }

    if (impossible) {
      printf("Case #%d: IMPOSSIBLE\n", tc);
      continue;
    }

    int result = 0;

    for (int y = 0; y < H; y++) {
      for (int x = 0; x < W; x++) {
        if (grid[y][x] == '<') result++;
        if (grid[y][x] != '.') break;
      }
      for (int x = W-1; x >= 0; x--) {
        if (grid[y][x] == '>') result++;
        if (grid[y][x] != '.') break;
      }
    }

    for (int x = 0; x < W; x++) {
      for (int y = 0; y < H; y++) {
        if (grid[y][x] == '^') result++;
        if (grid[y][x] != '.') break;
      }
      for (int y = H-1; y >= 0; y--) {
        if (grid[y][x] == 'v') result++;
        if (grid[y][x] != '.') break;
      }
    }

    printf("Case #%d: %d\n", tc, result);
  }
}
