#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
const int N=202;
int n,k;
double dp[N][N];
double pp[N*2];
double aa[N];
double fun(int l,int r){
    for(int i=1;i<=k;i++)aa[i]=pp[i-1+l];
    memset(dp,0,sizeof(dp));
    dp[0][0]=1;
    for(int i=1;i<=k;i++){
        for(int j=0;j<=k;j++){
            if(j)dp[i][j]=dp[i-1][j]*(1-aa[i])+dp[i-1][j-1]*aa[i];
            else dp[i][j]=dp[i-1][j]*(1-aa[i]);
        }
    }
    return dp[k][k/2];
}

int main(){
    #ifdef DouBi
    freopen("in.cpp","r",stdin);
    freopen("out.cpp","w",stdout);
    #endif // DouBi
    int T;scanf("%d",&T);
    int cas=1;
    while(T--){
        printf("Case #%d: ",cas++);
        scanf("%d%d",&n,&k);
        for(int i=1;i<=n;i++)scanf("%lf",&pp[i]);
        sort(pp+1,pp+n+1);
        for(int i=1;i<=n;i++)pp[i+n]=pp[i];
        double ans=0;
        for(int i=k;i<=2*n;i++){
            ans=max(ans,fun(i-k+1,i));
        }
        printf("%.10lf\n",ans);
    }
    return 0;
}
