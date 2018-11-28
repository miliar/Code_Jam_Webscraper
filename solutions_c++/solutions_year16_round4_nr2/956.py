#include <bits/stdc++.h>
#define FOR(i, n) for (int i = 0; i < (n); ++i)
#define REP(i, n) for (int i = 1; i <= (n); ++i)
using namespace std;

int T, N, K;
double A[201], dpL[201][201], dpR[201][201];

void calculate(double dp[201][201]) {
  for (int i = 0; i <= K; ++i) dp[0][i] = 0.0;
  dp[0][0] = 1.0;
  for (int k = 1; k <= K; ++k) {
    for (int i = 0; i <= K; ++i) {
      dp[k][i] = dp[k - 1][i] * (1.0 - A[k]);
      if (i - 1 >= 0) dp[k][i] += dp[k - 1][i - 1] * A[k];
    }
  }
}

int main() {
  scanf("%d", &T);
  REP (tc, T) {
    scanf("%d%d", &N, &K);
    REP (i, N) scanf("%lf", &A[i]);

    sort(A + 1, A + N + 1);

    calculate(dpL);
    reverse(A + 1, A + N + 1);
    calculate(dpR);

    double best = 0.0;
    for (int kl = 0; kl <= K; ++kl) {
      double cur = 0.0;
      for (int k = 0; k <= K / 2; ++k)
        cur += dpL[kl][k] * dpR[K - kl][K / 2 - k];
      best = max(best, cur);
    }

    printf("Case #%d: %.10lf\n", tc, best);
  }
  return 0;
}
