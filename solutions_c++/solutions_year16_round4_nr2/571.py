/*
 * Author:王禹秋(jywyq) 
 * Date:20160528
 */
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<string>
#include<cstring>
using namespace std;
#define LL long long
double dp[210][210];//取i个人有j个人投票yes的概率 
double a[210];
int main(){
	freopen("B-large.in","r",stdin);
	freopen("dataout.txt","w",stdout);
	int t,cas=0,K,N;
	cin>>t;
	while(t--){
		cin>>N>>K;
		for(int i=1;i<=N;i++){
			cin>>a[i];
		}
		sort(a+1,a+1+N);
		memset(dp,0,sizeof dp);
		dp[0][0]=1.0;
		for(int i=1;i<=N;i++){
			dp[i][0]=dp[i-1][0]*(1-a[i]);
			for(int j=1;j<=i;j++){
				dp[i][j]=dp[i-1][j]*(1-a[i])+dp[i-1][j-1]*a[i];
			}
		}
		double ans=0;
		for(int l=K;~l;l--){
            for(int j=N-(K-l)+1,i=l+1;j<=N;i++,j++){
                dp[i][0]=dp[i-1][0]*(1-a[j]);
                for(int k=1;k<=i;k++)
                    dp[i][k]=dp[i-1][k-1]*a[j]+dp[i-1][k]*(1-a[j]);
            }
            ans=max(ans,dp[K][K/2]);
        }
		printf("Case #%d: %.13lf\n",++cas,ans);
		
		
	}
}
