#include<bits/stdc++.h>
using namespace std;
int n,K;
double p[222];
double dp[222][222];
void solve(){
    scanf("%d%d",&n,&K);
    for(int i=1;i<=n;i++)scanf("%lf",p+i);
    sort(p+1,p+n+1);
    double ans=0;
    for(int i=0;i<=K;i++){
        memset(dp,0,sizeof(dp));
        dp[0][0]=1;
        for(int j=1;j<=K;j++){
            double w=j<=i?p[j]:p[n-(j-i)+1];
            for(int k=0;k<=K;k++){
                dp[j][k]=dp[j-1][k]*(1-w);
                if(k)dp[j][k]+=dp[j-1][k-1]*w;
            }
        }
        ans=max(ans,dp[K][K>>1]);
    }
    printf("%.12f\n",ans);
}
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int cas=1;
    int _;scanf("%d",&_);
    while(_--){
        printf("Case #%d: ",cas++);
        solve();
    }
}
