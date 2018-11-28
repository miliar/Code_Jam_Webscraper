#include "stdio.h"
#include "iostream"
#include "vector"
#include "queue"
#include "algorithm"
#include "deque"
using namespace std;

int main() {
  cout.sync_with_stdio(false);
  int T;
  cin>>T;
  for (int cs = 1; cs<= T;cs++) {
    cout <<"Case #"<<cs<<": ";
    vector<double> p;
    int N,K;
    cin >> N>>K;
    for (int i = 0; i<N;i++) {
      double tmp;
      cin >> tmp;
      p.push_back(tmp);
    }
    sort(p.begin(), p.end());
    double ans = 0;
    for (int i = 0; i<=K;i++) {
      double t[250];
      for (int j= 1; j<=K;j++) {
        if (j<=i) {
          t[j] = p[j-1];
        }
        else {
          t[j] = p[N+i-j];
        }
        // cout << t[j] << " ";
      }
      // cout << endl;
      double dp[250][250] = {};
      dp[0][0] = 1;
      for (int j = 1; j<=K; j++) {
        for (int k = 0; k<=j; k++) {
          if (k==0) {
            dp[j][k] = max(dp[j][k], dp[j-1][k] * (1-t[j]));
          }
          else {
            dp[j][k] = max(dp[j][k], dp[j-1][k-1] * t[j] + dp[j-1][k] * (1-t[j]));
          }
          // cout << j << " " << k << " " << dp[j][k] << endl;
        }
      }
      ans = max(ans, dp[K][K/2]);
    }
    cout << ans << endl;
  }
  return 0;
}
