#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

int T,N,K;
double p[500];
double f[500][300];
double d[500],ans;

int main() {
	freopen("2A.in","r",stdin);
	freopen("2A.out","w",stdout);
	scanf("%d",&T);
	for (int kase = 1;kase <= T; kase++) {
		scanf("%d%d",&N,&K);
		for (int i = 1; i <= N; i++)
				scanf("%lf",&p[i]);
		sort(p+1,p+N+1);
		double ans = 0;
		for (int i = 0;i <= K; i++) {
			memset(f,0,sizeof f);
			f[0][0] = 1;
			for (int k = 1;k <= K; k++) {
				double bt = 0;
				if (k <= i) bt = p[k]; else bt = p[N-(k-i)+1];
				f[k][0] = (1-bt) * f[k-1][0];
				for (int l = 1;l <= k; l++)
					f[k][l] = bt * f[k-1][l-1] + (1-bt) * f[k-1][l];
			}
			ans = max(ans,f[K][K/2]);
		}
		
		printf("Case #%d: %lf\n",kase,ans);
	}
	return 0;
}