#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAXN = 110;
const int dx[4] = {0, 1, 0, -1};
const int dy[4] = {1, 0, -1, 0};
const char dz[] = ">v<^";

char s[MAXN][MAXN];
int d[MAXN][MAXN];

int main() {
  int re;

  scanf("%d", &re);
  for (int ri = 1; ri <= re; ++ri) {
    int r, c;

    scanf("%d%d", &r, &c);
    for (int i = 0; i < r; ++i) {
      scanf("%s", s[i]);
    }
    fill(d[0], d[r], 0);

    for (int i = 0; i < r; ++i) {
      for (int j = 0, k = -1; j < c; ++j) {
        if (s[i][j] != '.') {
          if (k != -1) {
            d[i][j] |= 1 << 2;
            d[i][k] |= 1 << 0;
          }
          k = j;
        }
      }
    }

    for (int j = 0; j < c; ++j) {
      for (int i = 0, k = -1; i < r; ++i) {
        if (s[i][j] != '.') {
          if (k != -1) {
            d[i][j] |= 1 << 3;
            d[k][j] |= 1 << 1;
          }
          k = i;
        }
      }
    }

    int ans = 0;
    for (int i = 0; i < r; ++i) {
      for (int j = 0; j < c; ++j) {
        if (s[i][j] != '.') {
          int k = find(dz, dz + 4, s[i][j]) - dz;
          if (d[i][j] & (1 << k)) {
            ans += 0;
          } else if (d[i][j] != 0) {
            ans += 1;
          } else {
            ans = r * c + 1;
          }
        }
      }
    }

    printf("Case #%d: ", ri);
    if (ans <= r * c) {
      printf("%d\n", ans);
    } else {
      puts("IMPOSSIBLE");
    }
  }

  return 0;
}
