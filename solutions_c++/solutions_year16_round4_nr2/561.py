#include <bits/stdc++.h>
using namespace std;
#define LL long long
#define PB push_back
double p[220];
vector<double>A;
int n,k;
double dp[220][220];
double solve(int pre,int m){
    A.clear();
    for (int i = 0 ; i < pre ; ++i) A.PB(p[i]);
    int last = m - pre;
    for (int j = n - 1 ; last ; --j , --last) A.PB(p[j]);
    memset(dp,0,sizeof dp);
    dp[1][1] = A[0];
    dp[1][0] = 1. - A[0];
    for (int i = 1 ; i < m ; ++i){
        for (int j = 0 ; j <= i ; ++j){
            dp[i + 1][j + 1] += dp[i][j] * A[i];
            dp[i + 1][j] += dp[i][j] * (1. - A[i]);
        }
    }
    return dp[m][m / 2];
}
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int t,cas=1;
    scanf("%d",&t);
    while(t--){
        cin>>n>>k;
        for(int i=0;i<n;i++) cin>>p[i];
        sort(p,p+n);
        double ans=0;
        for(int i=0;i<=k;i++){
            ans=max(ans,solve(i,k));
        }
        printf("Case #%d: %.6lf\n",cas++,ans);
    }
    return 0;
}
