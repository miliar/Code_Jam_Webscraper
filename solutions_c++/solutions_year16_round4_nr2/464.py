#include <bits/stdc++.h>
using namespace std;

#define mp(x, y) make_pair((x), (y))

typedef long long ll;

int q;

int n, k;
double p[222];
double pr[222];
double dp[222][222][222];

double tie()
{
	for(int i=0; i<k; i++) {
		dp[i][i][0]=pr[i];
		dp[i][i][1]=1.0-pr[i];
	}
	for(int i=0; i<k; i++) {
		for(int j=i+1; j<k; j++) {
			for(int l=0; l<=j-i+1; l++) {
				if(l>0) dp[i][j][l]=pr[j]*dp[i][j-1][l]+(1.0-pr[j])*dp[i][j-1][l-1];
				else dp[i][j][l]=pr[j]*dp[i][j-1][l];
			}
		}
	}
	return dp[0][k-1][k/2];
}

int main()
{
	scanf("%d\n", &q);

	for(int x=1; x<=q; x++) {
		scanf("%d%d", &n, &k);
		for(int i=0; i<n; i++) scanf("%lf", &p[i]);
		sort(p, p+n);
		double ans=0.0;
		for(int i=0; i<n; i++) {
			double cur;
			int cnt=0;
			for(int j=0; j<i; j++) pr[cnt++]=p[j];
			for(int j=n-1; cnt<k; j--) pr[cnt++]=p[j];
			if(cnt!=k) continue;
			sort(pr, pr+k);
			ans=max(ans, tie());
		}
		printf("Case #%d: %.12lf\n", x, ans);
	}

	return 0;
}
