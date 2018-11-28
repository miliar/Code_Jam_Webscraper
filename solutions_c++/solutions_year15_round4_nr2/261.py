#include <cstdio>
#include <algorithm>
using namespace std;

#define N 128
#define eps 1e-10
#define eps2 1e-15

int T, n, p[N];
double tv, tc, r[N], c[N], t[N], lo, md, hi, tr;

bool ok(double t) {
	double mx = 0, mn = 0, cv = 0;
	for (int i = 0; i < n; ++i) {
		if (cv + t*r[i] <= tv) {
			cv += t*r[i];
			mn += t*r[i]*c[i];
		} else {
			mn += (tv - cv)*c[i];
			break;
		}
	}
	cv = 0;
	for (int i = n - 1; i >= 0; --i) {
		if (cv + t*r[i] <= tv) {
			cv += t*r[i];
			mx += t*r[i]*c[i];
		} else {
			mx += (tv - cv)*c[i];
			break;
		}
	}
	return (tc*tv < mx*(1 + eps2) && mn < tc*tv*(1 + eps2));
}

bool cmp(int a, int b) {
	return c[a] < c[b];
}

int main() {
	scanf("%d", &T);
	for (int ca = 1; ca <= T; ++ca) {
		printf("Case #%d: ", ca);
		scanf("%d%lf%lf", &n, &tv, &tc);
		tr = 0;
		for (int i = 0; i < n; ++i) {
			scanf("%lf%lf", r + i, c + i);
			if (c[i] == tc) {
				tr += r[i];
				--n;
				--i;
			}
		}
		for (int i = 0; i < n; ++i)
			p[i] = i;
		sort(p, p + n, cmp);
		for (int i = 0; i < n; ++i)
			t[i] = c[p[i]];
		for (int i = 0; i < n; ++i)
			c[i] = t[i];
		for (int i = 0; i < n; ++i)
			t[i] = r[p[i]];
		for (int i = 0; i < n; ++i)
			r[i] = t[i];
		if (!ok(1e8)) {
			if (tr < eps) puts("IMPOSSIBLE");
			else printf("%.8f\n", tv / tr);
			continue;
		}
		lo = 0; hi = 1e8;
		while (hi - lo > eps*lo && hi - lo > eps) {
			md = .5*(lo + hi);
			if (ok(md)) hi = md;
			else lo = md;
		}
		lo = tv / (tv / lo + tr);
		printf("%.8f\n", lo);
	}
	return 0;
}
