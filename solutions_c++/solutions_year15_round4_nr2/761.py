#include <bits/stdc++.h>
using namespace std;
const int maxn = 105;
double v[maxn], x[maxn];
double eps = 1e-8;
bool equ(double a, double b) {
	return fabs(a - b) < eps;
}
int main() {
#ifdef youmu
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.ou", "w", stdout);
#endif
	int T, n, cases = 0;
	double V, X;
	cin >> T;
	while(T--) {
		cin >> n >> V >> X;
		for(int i = 0; i < n; i++) {
			cin >> v[i] >> x[i];
		}
		printf("Case #%d: ", ++cases);
		if(n == 1) {
			if(!equ(X, x[0])) {
				printf("IMPOSSIBLE\n");
			} else {
				printf("%.10f\n", V / v[0]);
			}
		} else {
			double ans = 1e15, l = 0, r = V;
			if(equ(x[0], x[1])) {
				if(equ(x[0], X)) {
					printf("%.10f\n", V / (v[0] + v[1]));
				} else {
					printf("IMPOSSIBLE\n");
				}
			} else {
				double t = (X * V - V * x[1]) / (x[0] - x[1]);
				
				if(t >= 0 && t <= V + eps) {
					printf("%.10f\n", max(t / v[0], (V - t) / v[1]));
				}  else {
					printf("IMPOSSIBLE\n");
				}
			}
		}
	}
	return 0;
}
