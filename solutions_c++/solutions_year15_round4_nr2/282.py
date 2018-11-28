#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;
const int N = 105;
double vv, cc, v[N], c[N];
#define eps 1e-10
#define F first
#define S second
pair<double, double> a[N];
int n;
bool check(double x) {
	double xx = 0.0, yy = 0.0;
	double t = vv;
	for (int i = n; i >= 1; --i) {
		if (x * a[i].S <= t || fabs(x * a[i].S - t) <= eps) {
			xx += x * a[i].F * a[i].S;
			yy += x * a[i].S;
			t -= x * a[i].S;
		}
		else xx += t * a[i].F, yy += t, t = 0.0;
	}
	if (t > eps)	return 0;
	double now = xx / yy;
	t = vv, xx = 0.0, yy = 0.0;
	for (int i = 1; i <= n; ++i) {
		if (x * a[i].S <= t || fabs(x * a[i].S - t) <= eps) {
			xx += x * a[i].F * a[i].S;
			yy += x * a[i].S;
			t -= x * a[i].S;
		}
		else xx += t * a[i].F, yy += t, t = 0.0;
	}
	double now2 = xx / yy;
	return (cc <= now || (fabs(cc - now) <= eps)) && (cc >= now2 || fabs(cc - now2) <= eps);
}
int main() {
	int T;
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d", &T);
	int cas=0;
	while (T--) {
		++cas;
		printf("Case #%d: ",cas);
		scanf("%d", &n);
		scanf("%lf%lf", &vv, &cc);
		for (int i = 1; i <= n; ++i)	scanf("%lf%lf", &a[i].S, &a[i].F);
		sort(a + 1, a + n + 1);
		double l = 0, r = 1e8, ans = -1;
		for (int i = 1; i <= 1000; ++i) {
			double mid = (l + r) * 0.5;
			if (check(mid))	ans = r = mid;
			else l = mid;
		}
		if (fabs(ans + 1) < eps)	puts("IMPOSSIBLE");
		else	printf("%.9lf\n", ans);
	}
	return 0;
}

