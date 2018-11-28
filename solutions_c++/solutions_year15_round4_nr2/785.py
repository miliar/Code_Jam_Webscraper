#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
using namespace std;

void setIO(string name) {
	string in_f = name + ".in";
	string out_f = name + ".out";
	freopen(in_f.c_str(), "r", stdin);
	freopen(out_f.c_str(), "w", stdout);
}

const int N = 1111;
const long double eps = 1e-10;

int n;
long double V, X;
long double v[N],x[N];

int equal(long double a, long double b) {
	return a - eps < b && b < a + eps;
}

int main() {
	setIO("B");
	int TT;
	scanf("%d", &TT);
	for (int T = 1; T <= TT; ++T) {
		printf("Case #%d: ", T);
		fprintf(stderr, "Now solving %d\n", T);
		double VV, XX;
		scanf("%d %lf %lf", &n, &VV, &XX);
		V = VV, X = XX;
		X *= V;
		for (int i = 1; i <= n; ++i) {
			double vv, xx;
			scanf("%lf %lf", &vv, &xx);
			v[i] = vv, x[i] = xx;
			x[i] *= v[i];
		}
		if (n == 1) {
			if (!equal(x[1] / v[1], X / V)) puts("IMPOSSIBLE");
			else printf("%.10f\n", double(V / v[1]));
		}
		else {
			if (equal(v[1] / x[1], v[2] / x[2])) {
				if (equal(v[1] / x[1], V / X)) {
					printf("%.10f\n", double(V / (v[1] +v[2])));
				}
				else puts("IMPOSSIBLE");
				continue;
			}
			long double a1, a2;
			a1 = (V * x[2] - X * v[2]) / (v[1] * x[2] - v[2] * x[1]);
			a2 = (V * x[1] - X * v[1]) / (v[2] * x[1] - v[1] * x[2]);
			if (a1 < -eps || a2 < -eps) puts("IMPOSSIBLE");
			else printf("%.10f\n", double(max(a1, a2)));
		}
	}
	return 0;
}
