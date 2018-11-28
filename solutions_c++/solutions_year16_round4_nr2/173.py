#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

int tc;
int n,k;
double p[205];
double sel[205],dp[205][205];

int main() {
	scanf("%d",&tc);
	for (int t=1; t<=tc; t++) {
		scanf("%d%d",&n,&k);
		for (int i=0; i<n; i++)
			scanf("%lf",&p[i]);
		sort(p,p+n);
		double ret = 0;

		for (int i=0; i<=k; i++) {
			int cnt = 0;
			for (int j=0; j<i; j++)
				sel[cnt++] = p[j];
			for (int j=0; j<k-i; j++)
				sel[cnt++] = p[n-j-1];

			memset(dp,0,sizeof(dp));
			dp[0][0] = 1;
			for (int j=0; j<k; j++) {
				for (int x=0; x<=k; x++) {
					dp[j+1][x+1] += dp[j][x]*sel[j];
					dp[j+1][x] += dp[j][x]*(1-sel[j]);
				}
			}
			/*
			for (int j=0; j<=k; j++)
				printf("%f ",dp[k][j]);
			printf(" = %f\n",dp[k][k/2]);
			*/
			ret = max(ret,dp[k][k/2]);
		}
		printf("Case #%d: %.9f\n",t,ret);
	}
    return 0;
}
