#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<cstring>
using namespace std;
typedef long long LL;
const int N=1000000+10;
LL dp[2][N];
int E,R,n;
int vi[N];
void Max(LL &a,LL b){
    if (a==-1) a=b;
    else a=max(a,b);
}
void work(){
    memset(dp,-1,sizeof(dp));
    dp[0][E]=0;
    int pos=0;
    for (int i=0;i<n;i++){
        for (int j=0;j<=E;j++){
            if (dp[pos][j]==-1) continue;
            for (int k=0;k<=j;k++){
                if (j-k+R>=E)    Max(dp[pos^1][E],dp[pos][j]+(LL)k*vi[i]);
             else
                Max(dp[pos^1][j-k+R],dp[pos][j]+(LL)k*vi[i]);
            }
        }
        memset(dp[pos],-1,sizeof(dp[pos]));
        pos^=1;
    }
    LL ret=-1;
    for (int i=0;i<=E;i++) if (dp[pos][i]!=-1) Max(ret,dp[pos][i]);
    cout<<ret<<endl;

}
int main(){
    int T,cas=0;
   freopen("B-small-attempt3.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    while (T--){
        scanf("%d%d%d",&E,&R,&n);
        //cout<<E<<" "<<R<<" "<<n<<endl;
        for (int i=0;i<n;i++) scanf("%d",&vi[i]);
      //  cout<<vi[0]<<endl;
        printf("Case #%d: ",++cas);
        work();
    }

    return 0;
}
