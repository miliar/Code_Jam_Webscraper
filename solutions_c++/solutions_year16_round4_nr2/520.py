#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;
typedef long long ll;
int T,t,n,m;
double arr[210];
double dp[210][210],num[3],ans;
int main(){
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int i,j,k,l,r,pos;
    scanf("%d",&T);
    for(t=1;t<=T;t++){
        scanf("%d%d",&n,&m);
        for(i=1;i<=n;i++)
            scanf("%lf",&arr[i]);
        sort(arr+1,arr+1+n);
        dp[0][0]=1;
        ans=0;
        for(i=1;i<=m;i++){
            dp[i][0]=dp[i-1][0]*(1-arr[i]);
            for(j=1;j<=i;j++)
                dp[i][j]=dp[i-1][j-1]*arr[i]+dp[i-1][j]*(1-arr[i]);
        }

        for(l=m;l>=0;l--){
            pos=n-(m-l)+1;
            i=l+1;
            for(;pos<=n;i++,pos++){
                dp[i][0]=dp[i-1][0]*(1-arr[pos]);
                for(j=1;j<=i;j++)
                    dp[i][j]=dp[i-1][j-1]*arr[pos]+dp[i-1][j]*(1-arr[pos]);
            }
            ans=max(ans,dp[m][m/2]);
        }
        printf("Case #%d: %.7f\n",t,ans);
    }
}
