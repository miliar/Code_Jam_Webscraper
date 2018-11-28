#include <cstdio>
#include <algorithm>
using namespace std;

int n, k;
double p[300];
double f[300][300];
double calc(int L,int R) {
	f[0][0] = 1.0;
	for(int i=1; i<=n; ++i) {
		double pv = 0.0;
		if( i <= L ) pv = p[i];
		if( (n-i+1) <= R ) pv = p[i];
		f[i][0] = f[i-1][0] * (1.0 - pv);
		for(int j=1; j<=k; ++j)
			f[i][j] = f[i-1][j] * (1.0 - pv) + f[i-1][j-1] * pv;
	}
	return f[n][k/2];
}

int main() {
	int T, ics = 0;
	scanf("%d", &T);
	while(T--) {
		scanf("%d%d", &n, &k);
		for(int i=1; i<=n; ++i)
			scanf("%lf", &p[i]);
		sort(p+1, p+n+1);
		double mx = 0.0;
		for(int i=0; i<=k; ++i)
			mx = max(calc(i, k-i), mx);
		printf("Case #%d: %.12f\n", ++ics, mx);
	}
	return 0;
}