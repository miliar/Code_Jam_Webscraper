#include <stdio.h>
#include <assert.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <functional>
#include <stack>
#include <string>

using namespace std;

#define inf 1000000007
#define rep(i, n) for(int i = 0; i < n; i++)

typedef long long ll;

double d[222];
double dp[222], dpw[222];

int main() {
  int t;
  scanf("%d",&t);
  for(int tt = 1; tt <= t; tt++) {
    int n, k;
    scanf("%d%d",&n,&k);
    rep(i, n) {
      scanf("%lf", d + i);
    }
    sort(d, d + n);
    double ma = 0.0;
    int e = n - k;
    rep(r, n - e + 1) {
      rep(i, n) {
        dp[i] = 0.0;
      }
      dp[0] = 1.0;
      rep(i, n) {
        if(r <= i && i < r + e) {
          continue;
        }
        rep(j, n + 1) {
          dpw[j] = 0;
        }
        rep(j, n) {
          dpw[j] += dp[j] * (1.0 - d[i]);
          dpw[j + 1] += dp[j] * d[i];
        }
        rep(j, n + 1) {
          dp[j] = dpw[j];
        }
      }
      ma = max(ma, dp[k / 2]);
    }
    printf("Case #%d: %0.9lf\n", tt, ma);
  }
}
