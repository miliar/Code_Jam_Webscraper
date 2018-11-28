/* 
  2014.03.26 15:10
  http://codeforces.ru/gym/100289/
*/


#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cmath>
#include <memory.h>
#include <cmath>
#include <string> 
#include <ctime>

using namespace std;

// #undef Fdg_Home

int h[132], g[132];
int dp[132][15 * 131 + 5];

void solveTest(int CS) {
  printf("Case #%d: ", CS);
  int p, q, n;
  scanf("%d%d%d", &p, &q, &n);
  for (int i = 0; i < n; ++i) {
    scanf("%d%d", &h[i], &g[i]);
  }
  memset(dp, -1, sizeof(dp));
  dp[0][1] = 0;
  for (int i = 0; i < n; ++i) {
    for (int s = 0; s <= n * 11; ++s) {
      if (dp[i][s] != -1) {
        dp[i + 1][s + (h[i] + q - 1) / q] = max(dp[i + 1][s + (h[i] + q - 1) / q], dp[i][s]);

        int can = h[i] / q, need = h[i] % q;
        if (h[i] % q == 0) --can, need += q;
        need = (need + p - 1) / p;
        int ns = s + can;
        if (ns >= need)
          dp[i + 1][ns - need] = max(dp[i + 1][ns - need], dp[i][s] + g[i]);
      }
    }
  }
  int ans = 0;
  for (int s = 0; s <= n * 11; ++s)
    ans = max(ans, dp[n][s]);
  printf("%d\n", ans);
}

int main() {
// #ifndef Fdg_Home
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
// #endif
  int T;
  scanf("%d\n", &T);
  for (int test = 1; test <= T; ++test) {
    solveTest(test);
  }
  return 0;
}