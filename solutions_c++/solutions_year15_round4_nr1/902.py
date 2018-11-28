#include <cstdio>
#include <cstring>

char a[8] = "<>^v";
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

int r, c;
char s[1024][1024];

int ok(int i, int j, int tp) {
  int ni = i + dx[tp];
  int nj = j + dy[tp];
  while (ni >= 0 && ni < r && nj >= 0 && nj < c && s[ni][nj] == '.') {
    ni += dx[tp];
    nj += dy[tp];
  }
  if (ni >= 0 && ni < r && nj >= 0 && nj < c) {
    return true;
  }
  return false;
}

int main() {
  int t, T;
  scanf("%d", &T);
  for (t = 1; t <= T; ++t) {
    scanf("%d %d", &r, &c);
    for (int i = 0; i < r; ++i) {
      scanf("%s", s[i]);
    }
    int ans = 0;
    bool imp = 0;
    for (int i = 0; i < r; ++i) {
      for (int j = 0; j < c; ++j) {
        for (int tp = 0; tp < 4; ++tp) {
          if (s[i][j] == a[tp]) {
            if (!ok(i, j, tp)) {
              bool o = false;
              for (int l = 0; l < 4; ++l) {
                if (ok(i, j, l)) {
                  o = true;
                }
              }
              if (!o) {
                imp = 1;
              }
              ++ans;
            }
          }
        }
      }
    }
    if (imp) {
      printf("Case #%d: IMPOSSIBLE\n", t);
    } else {
      printf("Case #%d: %d\n", t, ans);
    }
  }
  return 0;
}
