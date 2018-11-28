#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

double p[210],f[210][210],A[210];
int t,T,n,k;
double ans;

double count() {
	memset(f,0,sizeof(f));
	f[0][0] = 1;
	for (int i = 1; i <= k; i++) {
		f[i][0] = f[i - 1][0] * A[i];
		for (int j = 1; j <= i; j++)
			f[i][j] = f[i - 1][j] * A[i] + f[i - 1][j - 1] * (1.0 - A[i]);
	}
	return f[k][k / 2];
}

int main() {
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	for (scanf("%d",&T), t = 1; t <= T; t++) {
		printf("Case #%d: ", t);
		scanf("%d %d",&n,&k);
		for (int i = 1; i <= n; i++) scanf("%lf",&p[i]);
		sort(p + 1, p + n + 1);
		ans = 0;
		for (int i = 0; i <= k; i++) {			
			for (int j = 1; j <= i; j++) A[j] = p[j];
			for (int j = n; j > n - (k - i); j--) A[i + 1 + n - j] = p[j];			
			ans = max(ans,count());
		}
		printf("%.10lf\n",ans);
	}
	return 0;
}
