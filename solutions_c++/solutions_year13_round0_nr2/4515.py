#include <stdio.h>
#include <assert.h>

int n, m;
int map[100][100];
bool possible[100][100];

void cut (int x, int y, int dx, int dy) {
  int max = 0;
  for (int i = x, j = y; i < n && j < m; i += dx, j += dy) {
    if (map[i][j] > max) {
      max = map[i][j];
    }
  }
  for (int i = x, j = y; i < n && j < m; i += dx, j += dy) {
    if (map[i][j] == max) {
      possible[i][j] = true;
    }
  }
}

bool possib () {
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (!possible[i][j]) {
        return false;
      }
    }
  }
  return true;
}

int main (void) {
  int T;
  int scanned = scanf("%d", &T);
  for (int currentcase = 1; currentcase <= T; ++currentcase) {
    scanf("%d", &n);
    scanf("%d", &m);
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        scanf("%d", &map[i][j]);
        possible[i][j] = false;
      }
    }
    for (int i = 0; i < n; i++) {
      cut(i, 0, 0, 1);
    }
    for (int i = 0; i < m; i++) {
      cut(0, i, 1, 0);
    }
    printf("Case #%d: %s\n", currentcase, possib() ? "YES" : "NO");
  }
  return 0;
}
