#include <bits/stdc++.h>
using namespace std;
double a[500];
double dp[20][9];
int main(){
	freopen("b.txt","r",stdin);
	freopen("bbout.txt","w",stdout);
	int T,ca=0;
	scanf("%d",&T);
	while(T--){
		int n,k;
		scanf("%d%d",&n,&k);
		for (int i=0;i<n;i++)
			scanf("%lf",&a[i]);
		printf("Case #%d: ", ++ca);
		double ans=0;
		dp[0][0]=1;
		for (int i=3;i<(1<<n);i++){
			int cnt=0;
			for (int j=0;j<n;j++)
				if ((1<<j)&i) cnt++;
			if (cnt-k) continue;
			cnt=0;
			for (int j=0;j<n;j++)
				if ((1<<j)&i) {
					cnt++;
					memset(dp[cnt],0,sizeof dp[cnt]);
					for (int l=0;l<=k/2;l++){
						dp[cnt][l]+=dp[cnt-1][l]*(1-a[j]);
						if (l) dp[cnt][l]+=dp[cnt-1][l-1]*a[j];
					}
				}
			ans=max(ans,dp[cnt][k/2]);
		}
		printf("%.10f\n",ans );
	}
	return 0;
}