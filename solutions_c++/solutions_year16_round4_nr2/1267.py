#include <bits/stdc++.h>

#define REP(i,n)    for(int i=0;i<(n);++i)

using namespace std;

int main() {
  int t;
  cin>>t;
  REP(cnt,t){
    int n,k;
    cin>>n>>k;
    vector<double> cm(n);
    REP(i,n)
      cin>>cm[i];
    double mx = 0;
    REP(i,1<<n) {
      vector<double> sl;
      REP(j,n){
        if ((i>>j)&1) sl.push_back(cm[j]);
      }
      if (sl.size()!=k) continue;
      vector<vector<double>> dp(k, vector<double>(k+1, 0));
      dp[0][0] = 1-sl[0];
      dp[0][1] = sl[0];
      for(int j=1;j<k;++j) {
        REP(l,j+2){
          dp[j][l] = dp[j-1][l] * (1-sl[j]);
          if (l) dp[j][l] += dp[j-1][l-1] * sl[j];
        }
      }
      mx = max(mx, dp[k-1][k/2]);
    }
    cout<<"Case #"<<(cnt+1)<<": "<<fixed<<setprecision(10)<<mx<<endl;
  }
  return 0;
}
