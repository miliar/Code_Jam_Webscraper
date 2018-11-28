#include <iostream>
#include <cstdlib>
#include <cassert>
#include <vector>
using namespace std;

double p[211];

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int N, K; cin >> N >> K;
    for (int i = 0; i < N; i++) {
      cin >> p[i];
    }
    sort(p, p+N);

    double best = 0;
    for (int i = 0; i <= N && i <= K; i++) {
      vector<double> a;
      for (int j = 0; j < i; j++) {
        a.push_back(p[j]);
      }
      for (int j = N-1; j >= N-(K-i); j--) {
        a.push_back(p[j]);
      }
      assert(a.size() == K);

      double dp[211][211] = {0};
      dp[0][0] = 1;
      for (int j = 0; j < K; j++) {
        for (int k = 0; k <= j; k++) {
          if (dp[j][k]) {
            dp[j+1][k] += dp[j][k] * (1-a[j]);
            dp[j+1][k+1] += dp[j][k] * a[j];
          }
        }
      }
      best = max(best, dp[K][K/2]);
    }

    printf("Case #%d: %.06lf\n", t, best);
  }
}
