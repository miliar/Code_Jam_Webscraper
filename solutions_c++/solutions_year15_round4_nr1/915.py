#include <stdio.h>

const int RCMAX = 100;


int R, C;
char mp[RCMAX][RCMAX + 1];
int count[RCMAX][RCMAX];

int main() {
  int t, T;
  for (scanf("%d", &T), t = 1; t <= T; ++t) {
    printf("Case #%d: ", t);

    scanf("%d %d", &R, &C);
    for (int r = 0; r < R; ++r) {
      scanf("%s", mp[r]);
    }

    for (int r = 0; r < R; ++r) {
      for (int c = 0; c < C; ++c) {
        count[r][c] = 0;
      }
    }

    int ans = 0;
    for (int r = 0; r < R; ++r) {
      int c;
      c = 0;
      while (c < C && mp[r][c] == '.') {
        ++c;
      }
      if (c < C) {
        count[r][c] += 1;
        if (mp[r][c] == '<') {
          ans += 1;
        }
      }
      c = C - 1;
      while (0 <= c && mp[r][c] == '.') {
        --c;
      }
      if (0 <= c) {
        count[r][c] += 1;
        if (mp[r][c] == '>') {
          ans += 1;
        }
      }
    }
    for (int c = 0; c < C; ++c) {
      int r;
      r = 0;
      while (r < R && mp[r][c] == '.') {
        ++r;
      }
      if (r < R) {
        count[r][c] += 1;
        if (mp[r][c] == '^') {
          ans += 1;
        }
      }
      r = R - 1;
      while (0 <= r && mp[r][c] == '.') {
        --r;
      }
      if (0 <= r) {
        count[r][c] += 1;
        if (mp[r][c] == 'v') {
          ans += 1;
        }
      }
    }

    bool bad = false;
    for (int r = 0; r < R && !bad; ++r) {
      for (int c = 0; c < C && !bad; ++c) {
        bad = (count[r][c] == 4);
      }
    }

    if (bad) {
      printf("IMPOSSIBLE\n");
    } else {
      printf("%d\n", ans);
    }
  }
  return 0;
}
