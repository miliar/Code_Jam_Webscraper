#include<bits/stdc++.h>
using namespace std;
char s[105];
int dp[105][2];
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B.out","w",stdout);
    int t,n,i,j,C=0;
    scanf("%d",&t);
    while(t--){
        scanf("%s",&s[1]);
        memset(dp,-1,sizeof(dp));
        dp[0][0]=dp[0][1]=0;
        for(i=1;s[i];i++){
            if(s[i]=='+'){
                dp[i][0]=dp[i-1][0];
                for(j=i;j>0;j--){
                    if(s[j]=='-') break;
                    if(dp[i][1]==-1 || dp[j-1][0]+1<dp[i][1]){
                        dp[i][1]=dp[j-1][0]+1;
                    }
                }
            }
            else{
                dp[i][1]=dp[i-1][1];
                for(j=i;j>0;j--){
                    if(s[j]=='+') break;
                    if(dp[i][0]==-1 || dp[j-1][1]+1<dp[i][0]){
                        dp[i][0]=dp[j-1][1]+1;
                    }
                }
            }
        }
        printf("Case #%d: %d\n",++C,dp[i-1][0]);
    }
}
