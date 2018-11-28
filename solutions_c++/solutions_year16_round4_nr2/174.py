#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
int n,k;
double a[222];
double dp[222][222];
double b[222];int lb;
double calc(){
		int n=k;
		memset(dp,0,sizeof(dp));
		dp[0][0] = 1;
		for(int i=0; i<n; i++)
			for(int j=0; j<=i; j++){
				dp[i+1][j+1] += dp[i][j] * b[i];
				dp[i+1][j] += dp[i][j] * (1-b[i]);
			}
		return dp[n][n/2];
}
int main(){
	int _;
	scanf("%d",&_);
	for(int T=1; T<=_; T++){
		scanf("%d%d",&n,&k);
		for(int i=0; i<n; i++){
			scanf("%lf",&a[i]);
		}
		sort(a,a+n);
		double res=0;
		for(int i=0; i<=k; i++){
			lb=0;
			for(int j=0; j<i; j++)
				b[lb++]=a[j];
			for(int j=0; j<k-i; j++)
				b[lb++]=a[n-1-j];
			res = max(res, calc());
		}
		printf("Case #%d: %.10lf\n",T,res);
	}
	return 0;
}