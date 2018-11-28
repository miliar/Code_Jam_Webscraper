// B. Cookie Clicker Alpha
#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define sz(a) (int)a.size()

const double eps = 1e-9;

double c, f, x;

double calc(double t) {
	double p = 2;
	int rep = 0;
	while (p*t<x && p*t >= c && (t-c/p)*(p+f) >= t*p + eps && rep < 100000) {
//		printf("t=%.5lf p=%.5lf\n", t, p);
		t -= c/p;
		p += f;
		rep++;
	}
	return t*p;
}

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; t++) {
		scanf("%lf %lf %lf", &c, &f, &x);

		double l = 0, r = x/2+1, ans = -1;
		for (int i = 0; i < 500; i++) {
			double m = (l+r)/2;
			if (calc(m) >= x+eps) {
				ans = m;
				r = m;
			} else {
				l = m;
			}
		}

		printf("Case #%d: %.7lf\n", t, ans);
	}

	return 0;
}