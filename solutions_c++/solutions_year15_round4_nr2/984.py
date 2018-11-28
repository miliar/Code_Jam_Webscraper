#include <cstdio>
#include <algorithm>
using namespace std;
const double eps = 1e-7;

int n;
double v, x, r[100], c[100];

double solve() {
	if (*max_element(c, c+n) + eps < x)
		return -1;
	if (*min_element(c, c+n) - eps > x)
		return -1;
	if (n == 1)
		return v / r[0];
	if (abs(c[1]-c[0]) < eps)
		return v/(r[0]+r[1]);
	double k0 = v*(x-c[0])/r[1]/(c[1]-c[0]);
	double k1 = v*(c[1]-x)/r[0]/(c[1]-c[0]);
	return max(k0, k1);
}

int main() {
	//freopen("input.txt", "r", stdin);
	freopen("r2\\B-small-attempt0.in", "r", stdin);
	freopen("r2\\B-small.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int N=1; N<=T; ++N) {
		scanf("%d%lf%lf", &n, &v, &x);
		for (int i=0; i<n; ++i)
			scanf("%lf%lf", r+i, c+i);
		double ans = solve();
		printf("Case #%d: ", N);
		if (ans == -1)
			puts("IMPOSSIBLE");
		else
			printf("%.10f\n", ans);
	}
}