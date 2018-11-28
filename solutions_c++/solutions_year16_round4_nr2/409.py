#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

int N, K;
double p[210];
double dp[210][210];
double v[210];

double calc() {
  memset(dp, 0, sizeof(dp));
  dp[0][0] = 1;
  for (int i = 1; i <= K; i++) {
    for (int j = 0; j <= i; j++) {
      if (j > 0) dp[i][j] += dp[i-1][j-1] * v[i];
      dp[i][j] += dp[i-1][j] * (1 - v[i]);
    }
  }
  return dp[K][K/2];
}

double solve() {
  sort(p, p+N);
  double ans = 0;
  for (int i = 0; i <= K; i++) {
    int c = 1;
    for (int j = 0; j < i; j++) v[c++] = p[j];
    for (int j = 0; j < K - i; j++) v[c++] = p[N-1-j];
    // printf("c = %d\n", c);
    ans = max(ans, calc());
  }
  return ans;
}

int main() {
  int T;
  scanf("%d", &T);
  for (int kase = 1; kase <= T; kase++) {
    scanf("%d%d", &N, &K);
    for (int i = 0; i < N; i++) scanf("%lf", &p[i]);
    printf("Case #%d: ", kase);
    printf("%.7f\n", solve());
  }
  return 0;
}
