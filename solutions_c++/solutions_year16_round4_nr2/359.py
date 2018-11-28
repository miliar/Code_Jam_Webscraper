#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef map<int, int> mii;
typedef set<int> si;
typedef map<string, int> msi;

ld prob[210];
ld dp[210][210][210];

int main() {
  ios_base::sync_with_stdio(false);
  cout.setf(ios::fixed);
  cout.precision(10);
  int tt;
  cin >> tt;
  for (int ttt = 1; ttt <= tt; ++ttt) {
    cout << "Case #" << ttt << ": ";
    int n, k;
    cin >> n >> k;
    for (int i = 0; i < n; ++i) cin >> prob[i];
    sort(prob, prob + n);
    dp[0][0][0] = 1;
    for (int y = 1; y <= n; ++y) dp[0][0][y] = 0;
    for (int i = 0; i < n; ++i) {
      for (int y = 0; y <= n; ++y) {
        dp[i + 1][0][y] = dp[i][0][y] * (1. - prob[i]) + (y == 0 ? 0 : dp[i][0][y - 1] * prob[i]);
      }
    }
    for (int i = 0; i <= n; ++i) {
      for (int j = 0; i + j < k; ++j) {
        for (int y = 0; y <= n; ++y) {
          dp[i][j + 1][y] = dp[i][j][y] * (1. - prob[n - 1 - j]) + (y == 0 ? 0 : dp[i][j][y - 1] * prob[n - 1 - j]);
        }
      }
    }
    ld mx = 0;
    for (int i = 0; i <= k; ++i) mx = max(mx, dp[i][k - i][k / 2]);
    cout << mx << endl;
  }
}