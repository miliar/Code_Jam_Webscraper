#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define ALL(a) (a).begin(), (a).end()
#define SZ(a) ((int) (a).size())

const int N = 16;

int n, k;
long double a[N];
long double dp[N + 1][N + 1][1<<N];

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int T;
  cin >> T;
  while (T--) {
    cin >> n >> k;
    for (int i = 0; i < n; i++) {
      cin >> a[i];
    }
    memset(dp, 0, sizeof(dp));
    dp[0][0][0] = 1;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j <= i; j++) {
        for (int k = 0; k < (1 << i); k++) {
          if (dp[i][j][k]) {
            dp[i + 1][j][k | (1 << i)] += dp[i][j][k] * (1.0 - a[i]);
            dp[i + 1][j + 1][k | (1 << i)] += dp[i][j][k] * a[i];
            dp[i + 1][j][k] += dp[i][j][k];
          }
        }
      }
    }
    long double ans = 0.0;
    for (int i = 0; i < (1 << n); i++) {
      if (__builtin_popcount(i) == k) {
        ans = max(ans, dp[n][k / 2][i]);
      }
    }
    static int caseNo = 1;
    cout << "Case #" << caseNo++ << ": " << fixed << setprecision(10) << ans << endl;
  }
  return 0;
}


