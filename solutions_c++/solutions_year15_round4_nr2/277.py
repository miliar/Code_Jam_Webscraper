#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <string>
#include <set>
#include <map>
using namespace std;
#define rep(i, n) for (int i = 0; i < n; i++)
#define kep(i, n) for (int i = 1; i <=n; i++)
#define N 1111
const long double eps = 1e-10;

int T, n;

long double v, x;
long double r[N], c[N];

bool equal(long double x, long double y) {
	return abs(x-y) < eps;
}

void solve() {
	double tt1, tt2;
	scanf("%d%lf%lf", &n, &tt1, &tt2);
	v = tt1; x = tt2;
	rep(i, n) {
		scanf("%lf%lf", &tt1, &tt2);
		r[i] = tt1; c[i] = tt2;
	}
	for (int i = 0; i < n; i++)
		for (int j = 0; j < i; j++)
			if (c[j] > c[i]) {
				swap(c[i], c[j]);
				swap(r[i], r[j]);
			}
	if ((c[n-1] < x && !equal(c[n-1], x))  || (c[0] > x && !equal(c[0], x))) {
			puts("IMPOSSIBLE");
			return;
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < i; j++) {
			if (equal(c[j], c[i])) {
				r[j] += r[i];
				r[i] = r[n-1];
				c[i] = c[n-1];
				--n;
				break;
			}
		}
	}
	long double t1 = 0, t2 = 0;
	rep(i, n) {
		t1 += r[i]*c[i];
		t2 += r[i];
	}
	int ll = 0, rr = n-1;
	long double ans, p;
	if (!equal(t1/t2, x)) {
		if (t1 > t2*x) {
			t1 -= r[rr]*c[rr];
			t2 -= r[rr];
			while (t1 > t2 * x && !equal(t1, t2 * x)) {
				--rr;
				t1 -= r[rr]*c[rr];
				t2 -= r[rr];
			}
			p = (x*t2-t1)/(r[rr]*c[rr]-x*r[rr]);
			ans = v/(t2+p*r[rr]);
		} else {
			t1 -= r[ll]*c[ll];
			t2 -= r[ll];
			while (t1 < t2 * x && !equal(t1, t2 * x)) {
				++ll;
				t1 -= r[ll]*c[ll];
				t2 -= r[ll];
			}
			p = (x*t2-t1)/(r[ll]*c[ll]-x*r[ll]);
			ans = v/(t2+p*r[ll]);
		}
	} else ans = v/t2;
	printf("%.10f\n", (double)ans);
}

int main() {
	scanf("%d", &T);
	kep(_, T) {
		printf("Case #%d: ", _);
		solve();
	}
}
