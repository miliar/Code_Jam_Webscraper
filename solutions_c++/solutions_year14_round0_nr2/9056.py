#include<cstdio>

int t;
double e;
long double c, g, r, cps, ans;

int main() {
//	freopen("B-L.in", "r", stdin);
//	freopen("B-L.out", "w", stdout);
	scanf("%d", &t);
	for (int zzz = 1 ; zzz <= t ; zzz++) {
		cps = 2;
		ans = 0;
		scanf("%Lf", &e);
		c = e;
		scanf("%Lf", &e);
		g = e;
		scanf("%Lf", &e);
		r = e;
		while ((r - c) / cps >= c / g) {
			ans += c / cps;
			cps += g;
		}
		printf("Case #%d: %.7Lf\n", zzz, (double) (ans + r / cps));
	}
	scanf("\n");
	return 0;
}
