#include <cstdio>
#include <algorithm>

using namespace std;

int main() {
  int re;
  int n, m;
  vector<int> x, y;
  vector<int> dp;

  scanf("%d", &re);
  for (int ri = 1; ri <= re; ++ri) {
    scanf("%d", &n);
    m = 0;
    x = vector<int>(n, 0);
    y = vector<int>(n, 0);
    for (int i = 0; i < n; ++i) {
      static char s[80];
      scanf("%s", s);
      for (int j = 0; j < n; ++j) {
        if (s[j] == '1') {
          ++m;
          x[i] |= 1 << j;
          y[j] |= 1 << i;
        }
      }
    }

    dp = vector<int>(1 << n, n * n);
    dp[0] = 0;
    for (int i = 0; i < (1 << n); ++i) {
      for (int j = i; j > 0; j = (j - 1) & i) {
        int d = __builtin_popcount(j);

        int yy = 0;
        for (int k = 0; k < n; ++k) {
          if (j & (1 << k)) {
            yy |= y[k];
          }
        }
        if (__builtin_popcount(yy) > d) {
          continue;
        }

        int xx = 0;
        for (int k = 0; k < n; ++k) {
          if (yy & (1 << k)) {
            xx |= x[k];
          }
        }
        if ((xx & j) != xx) {
          continue;
        }

        dp[i] = min(dp[i], dp[i ^ j] + d * d);
      }
    }
    printf("Case #%d: %d\n", ri, dp.back() - m);
  }

  return 0;
}
