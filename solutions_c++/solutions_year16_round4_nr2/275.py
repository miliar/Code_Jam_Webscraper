#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <queue>
#include <iostream>
#define PS system("pause");
using namespace std;
double dp[209][209];
int n,K;
double p[209];
double a[209];
double solve(){
	dp[0][0]=1;
	for(int i=1;i<=K;i++){
		for(int j=0;j<=i&&j<=K/2;j++){
			dp[i][j]=dp[i-1][j]*(1-a[i]);
			if(j)
				dp[i][j]+=dp[i-1][j-1]*a[i];
		}
	}
	return dp[K][K/2];
}
int main(){
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int tt,cot=1;
	scanf("%d",&tt);
	while(tt--){
		scanf("%d%d",&n,&K);
		for(int i=0;i<n;i++)
			scanf("%lf",&p[i]);
		sort(p,p+n);
		double ans=0;
		for(int i=0;i<n;i++){
			int tot=0;
			for(int j=0;j<K;j++){
				a[++tot]=p[(i+j)%n];
			}
			ans=max(ans,solve());
		}
		printf("Case #%d: %f\n",cot++,ans);
	}
	//PS;
	return 0;
}