#include <set>
#include <map>
#include <cstdio>
#include <vector>
#include <cstring>
#include <cassert>
#include <utility>
#include <algorithm>

using namespace std;

const int MAXN = 21;

long double dp[1 << MAXN], cnt[1 << MAXN];

bool test(int i, int j) {
  return ((i >> j) & 1) != 0;
}

int main() {
  int re, n, m;
  static char buf[80];

  scanf("%d", &re);
  for (int ri = 1; ri <= re; ++ri) {
    scanf("%s", buf);
    n = strlen(buf);
    fill(dp, dp + (1 << n), 0);
    fill(cnt, cnt + (1 << n), 0);
    m = 0;
    for (int i = 0; i < n; ++i) {
      if (buf[i] == 'X') {
        m |= 1 << i;
      }
    }
    cnt[m] = 1;

    for (int i = 0; i < (1 << n) - 1; ++i) {
      if (cnt[i] == 0) {
        continue;
      }
      // printf("dp[%d] = %Lf\n", i, dp[i]);
      vector<int> bits;
      for (int j = 0; j < n; ++j) {
        if (!test(i, j)) {
          bits.push_back(j);
        }
      }
      for (int j = 0, k = 0; j <= bits.back(); ++j) {
        cnt[i | (1 << bits[k])] += cnt[i];
        dp[i | (1 << bits[k])] += dp[i] + (n - (bits[k] - j)) * cnt[i];
        if (j == bits[k]) {
          ++k;
        }
      }
      for (int j = bits.back() + 1; j < n; ++j) {
        cnt[i | (1 << bits[0])] += cnt[i];
        dp[i | (1 << bits[0])] += dp[i] + (j - bits[0]) * cnt[i];
      }
    }

    printf("Case #%d: ", ri);
    printf("%.16Lf\n", dp[(1 << n) - 1] / cnt[(1 << n) - 1]);
    fflush(stdout);
  }

  return 0;
}

