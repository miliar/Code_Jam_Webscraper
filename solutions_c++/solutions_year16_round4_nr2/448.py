#include <cstdio>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <cstring>
#include <map>
#include <set>
#include <queue>
#define LL long long
#define MAXN 100050
using namespace std;
double d[202][202];
double p[202];
double a[202];
int main() {
	freopen("B-large.in", "r", stdin);
	freopen("outputA3.txt", "w", stdout);
	int ri = 0, tt;
	scanf("%d", &tt);
	while (tt--) {
		int n, k;
		scanf("%d%d", &n, &k);
		for (int i = 1; i <= n; ++i)
			scanf("%lf", &p[i]);
		sort(p + 1, p + 1 + n);

		double ans = 0;
		for (int x = 0; x <= k; ++x) {
			int y = k - x;
			int h = 0;
			for (int j = 1; j <= x; ++j)
				a[++h] = p[j];
			for (int j = 1; j <= y; ++j)
				a[++h] = p[n - j + 1];
			memset(d, 0, sizeof(d));
			d[0][0] = 1;
			for (int j = 1; j <= k; ++j) {
				for (int x = 0; x <= j; ++x) {
					d[j][x] = d[j - 1][x] * (1 - a[j]);
					if (x > 0)
						d[j][x] += d[j - 1][x - 1] * a[j];
				}
			}
			if (d[k][k / 2] > ans)
				ans = d[k][k / 2];
		}
//		printf("%lf\n",ans);
		for (int i = 1; i + k - 1 <= n; ++i) {
			int l = i, r = i + k - 1;
			for (int j = 1; j <= k; ++j) {
				a[j] = p[j + l - 1];
			}
			memset(d, 0, sizeof(d));
			d[0][0] = 1;
			for (int j = 1; j <= k; ++j) {
				for (int x = 0; x <= j; ++x) {
					d[j][x] = d[j - 1][x] * (1 - a[j]);
					if (x > 0)
						d[j][x] += d[j - 1][x - 1] * a[j];
				}
			}
//			if(i==2){
//				for(int j=1;j<=k;++j)
//					for(int x=0;x<=j;++x)
//						printf("%d %d %lf\n",j,x,d[j][x]);
//			}
			if (d[k][k / 2] > ans)
				ans = d[k][k / 2];
		}
//		printf("%lf\n",ans);
		printf("Case #%d: %.8lf\n", ++ri, ans);
	}
}
