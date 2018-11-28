using namespace std;
#include <bits/stdc++.h>

const int MN = 1111;

int run_task() {
  int n; cin >> n;
  vector<int> nu(n);
  for (int i = 0; i < n; ++i)
    cin >> nu[i];

  vector<vector<int> > dp(n + 1, vector<int>(MN));

  for (int i = 0; i < MN; ++i)
    dp[n][i] = i;

  for (int i =  n - 1; i  >= 0; --i) {
    for (int j = 0; j < MN; ++j) {
      dp[i][j] = MN;
      for (int k = 1; k <= nu[i]; ++k) {
        int div = (nu[i] + k - 1) / k;
        dp[i][j] = min(dp[i][j], dp[i + 1][max(j, div)] + k - 1);
      }
    }
  }

  return dp[0][0];
}

int main() {
  int tc;
  cin >> tc;
  for (int c = 0; c < tc; ++c) {
    printf("Case #%d: %d\n", c + 1, run_task());
  }
  return 0;
}
