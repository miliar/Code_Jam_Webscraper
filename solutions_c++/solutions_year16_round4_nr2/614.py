#include <iostream>
#include <algorithm>
#define maxn 203

using namespace std;

double dp[maxn+2][maxn+2][maxn+2];
int main() {

  int T, n,k;
  double p[maxn+1];
  cin>>T;

  for(int t=1; t<=T; t++) {
    cin>>n>>k;

    for(int i=0; i<n; i++) cin>>p[i];

    sort(p,p+n);

    dp[0][n][0]=1.0;
    for(int s=1; s<=n; s++) dp[0][n][s]=0.0;
    for(int i=1; i<=n; i++) {
      dp[i][n][0]=dp[i-1][n][0]*(1-p[i-1]);
      for(int s=1; s<=n; s++) 
        dp[i][n][s]=dp[i-1][n][s]*(1-p[i-1])+dp[i-1][n][s-1]*p[i-1];
    }

    for(int j=n-1; j>=0; j--) {
      dp[0][j][0]=dp[0][j+1][0]*(1-p[j]);
      for(int s=1; s<=n; s++) {
        dp[0][j][s]=dp[0][j+1][s]*(1-p[j])+dp[0][j+1][s-1]*p[j];
      }
      for(int i=1; i<=j; i++) {
        dp[i][j][0]=dp[i-1][j][0]*(1-p[i-1]);
        for(int s=1; s<=n; s++) 
          dp[i][j][s]=dp[i-1][j][s]*(1-p[i-1])+dp[i-1][j][s-1]*p[i-1];
      }
    }
    /*
   
    for(int i=0; i<n; i++) cout<<p[i]<<" ";
    cout<<endl;

    for(int s=0; s<=n; s++){
      for(int i=0; i<=n; i++) {
        for(int j=0; j<=n; j++) cout<<dp[i][j][s]<<" ";
        cout<<endl;
      }
      cout<<endl;
    }*/

    double mymax=0.0;

    for(int i=0; i<=k; i++) {
      //cout<<i<<" "<<(i+n-k)<<" "<<dp[i][i+n-k][k/2]<<endl;
      mymax=max(mymax, dp[i][i+n-k][k/2]);
    }

    cout<<"Case #"<<t<<": "<<mymax<<endl;
    cout.flush();
  }

  return 0;

}
