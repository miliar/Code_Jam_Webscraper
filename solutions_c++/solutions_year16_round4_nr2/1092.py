#include<stdio.h>

int cnt[1<<16];
double a[16];
double dp[18][18];
int n,m;
int idx[16];

int main() {
	int N,cs=0,i,j,k,c;
	double ret;
	for(i=1;i<(1<<16);i++) cnt[i]=cnt[i>>1]+(i&1);
	for(scanf("%d",&N);N--;) {
		scanf("%d %d",&n,&m);
		for(i=0;i<n;i++) scanf("%lf",&a[i]);
		for(ret=k=0;k<(1<<n);k++) if (cnt[k]==m) {
			for(i=0;i<=m;i++) for(j=0;j<=m;j++) dp[i][j]=0;
			dp[0][0]=1;
			for(i=c=0;i<n;i++) if (k&(1<<i)) idx[c++]=i;
			for(i=0;i<m;i++) for(j=0;j<=i;j++) {
				dp[i+1][j+1]+=dp[i][j]*a[idx[i]];
				dp[i+1][j]+=dp[i][j]*(1-a[idx[i]]);
			}
			if (dp[m][m/2]>ret) ret=dp[m][m/2];
		}
		printf("Case #%d: %.10lf\n",++cs,ret);
	}
	return 0;
}
