#include<bits/stdc++.h>
#include<unistd.h>
using namespace std ;
#define ll long long
#define N 200100
#define R 0
#define P 1
#define S 2
#define inf 0x3f3f3f3f

double dp[17][17];
double l[202];
int n,k;
double ans;
double p[202];
double gao(){
    memset(dp,0,sizeof dp);
    dp[0][0]=1;
    for (int i=1;i<=k;i++){
        int mxj=min(i,k);
        for (int y=0;y<=mxj;y++){
            if (y) dp[i][y] += dp[i-1][y-1]*l[i];
            dp[i][y] += dp[i-1][y]*(1-l[i]);
      //         cout<<i<<' '<<y<<' '<<dp[i][y]<<endl;
        }
    }
  //  cout<<dp[k][k/2]<<endl;
    return dp[k][k/2];
}
void dfs(int d,int s){
    if (d==k){
        ans=max(ans,gao());
        return;
    }
    for (int i=s;n-i+d+1>=k;i++){
        l[d+1]=p[i];
        dfs(d+1,i+1);
    }
    return;
}
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int T,cas=0;
    cin>>T;
    while (T--){
        ans=0;
        cin>>n>>k;
        for (int i=1;i<=n;i++) scanf("%lf",&p[i]);
        dfs(0,1);
        printf("Case #%d: %.8f\n",++cas,ans);
    }
}
