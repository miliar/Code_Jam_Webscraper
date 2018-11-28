#include<cstdio>

int tt, n;
double e1, e2, ans1, ans2, v, x, r1, c1, r2, c2;

int main() {
	freopen("B-small.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
	scanf("%d", &tt);
	for (int zzz = 1 ; zzz <= tt ; zzz++) {
		scanf("%d %lf %lf", &n, &v, &x);
		if (n == 1) {
			scanf("%lf %lf", &r1, &c1);
			if (c1 == x) printf("Case #%d: %.9lf\n", zzz, v/r1);
			else printf("Case #%d: IMPOSSIBLE\n", zzz);
		}
		else {
			scanf("%lf %lf", &r1, &c1);
			scanf("%lf %lf", &r2, &c2);
			if (c1 == c2) {
				if (x == c1) printf("Case #%d: %.9lf\n", zzz, v*1./(r1+r2));
				else printf("Case #%d: IMPOSSIBLE\n", zzz);
			}
			else {
				ans1 = v/r1*(c2-x)/(c2-c1);
				ans2 = v/r2*(c1-x)/(c1-c2);
//				printf("ans1 = %.9lf ans2 = %.9lf\n", ans1, ans2);
				if (ans1 < 0 || ans2 < 0) printf("Case #%d: IMPOSSIBLE\n", zzz);
				else printf("Case #%d: %.9lf\n", zzz, ans1 > ans2 ? ans1 : ans2);
			}
		}
	}
	scanf("\n");
	return 0;
}
