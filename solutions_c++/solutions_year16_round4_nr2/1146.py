#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef pair<int,int> pr;

double dp[205][205];
double p[205];
double a[205];
double ans;

int n,K;

void dfs(int t,int cnt){
    if (t==n){
        if (cnt==K){
            for (int i=0;i<=16;i++){
                for (int j=0;j<=16;j++){
                    dp[i][j]=0.0;
                }
            }
            dp[0][0]=1.0;
            for (int i=1;i<=K;i++){
                dp[i][0]=dp[i-1][0]*(1-a[i]);
                for (int j=1;j<=i&&j<=K/2;j++){
                    dp[i][j]=dp[i-1][j]*(1-a[i])+dp[i-1][j-1]*a[i];
                }
            }
            ans=max(ans,dp[K][K/2]);
        }
        return ;
    }
    if (cnt<K){
        a[cnt+1]=p[t];
        dfs(t+1,cnt+1);
    }
    dfs(t+1,cnt);
}

void solve(){
    scanf("%d%d",&n,&K);
    for (int i=0;i<n;i++){
        scanf("%lf",p+i);
    }
    ans=0;
    dfs(0,0);
    printf("%.8f\n",ans);
}

int main(){
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int kase=1;kase<=T;kase++){
        printf("Case #%d: ",kase);
        solve();
    }
    return 0;
}
