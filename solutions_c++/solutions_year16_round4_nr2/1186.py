#include <bits/stdc++.h>

using namespace std;
double dp[205][205];
double A[205];
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    int index=1;
    while(t--){
       int n,k;
       cin >> n >> k;
       //double A[n+1];
       for(int i=1;i<=n;++i)
        cin >> A[i];
       sort(A+1,A+n+1);
       vector<double> V;
      // int flag=1;

       double ma=0;
       for(int i=0;i<=k;++i){V.clear();
        for(int j=1;j<=i;++j){
            V.push_back(A[j]);
        }
        for(int j=n;j>n-k+i;--j){
            V.push_back(A[j]);
        }
        dp[0][0]=1.0;
        for(int j=1;j<=k;++j){dp[j][0]=0;
            double temp=V[j-1];
            for(int l=0;l<=min(j,k/2);++l){
                dp[j][l+1]=temp*dp[j-1][l];
                dp[j][l]+=(1-temp)*dp[j-1][l];
            }
        }
        ma=max(dp[k][k/2],ma);
       }

      printf("Case #%d: %.12f\n",index,ma);
      ++index;

    }

    return 0;
}
