#include<bits/stdc++.h>
using namespace std;
char s[222];
int dp[222][2];
int n;
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int _,cas=1;scanf("%d",&_);    
    while(_--){
        scanf("%s",s);
        printf("Case #%d: ",cas++);
        n=strlen(s);
        dp[0][0]=s[0]=='-'?0:1;
        dp[0][1]=s[0]=='+'?0:1;
        for(int i=1;i<n;i++){
            if(s[i]=='-'){
                dp[i][0]=min(dp[i-1][0],dp[i-1][1]+1);
                dp[i][1]=min(dp[i-1][0]+1,dp[i-1][1]+2);
            }
            else{
                dp[i][1]=min(dp[i-1][1],dp[i-1][0]+1);
                dp[i][0]=min(dp[i-1][1]+1,dp[i-1][0]+2);
            }
        }
        printf("%d\n",dp[n-1][1]);
    }
}
