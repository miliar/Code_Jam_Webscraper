#include <bits/stdc++.h>
using namespace std;

int n;
double v, x, r[10], c[10];

void solve(int ca) {
	printf("Case #%d: ", ca);
	cin >> n >> v >> x;
	for (int i = 0; i < n; i++) cin >> r[i] >> c[i];
	if (n == 1) {
		if (abs(c[0] - x) < 1e-9) {
			double ans = v / r[0];
			printf("%.9f\n", ans);
		} else
			puts("IMPOSSIBLE");
		return ;
	}
	if (n == 2) {
		if (c[0] < x && c[1] < x || c[0] > x && c[1] > x) {
			puts("IMPOSSIBLE");
			return ;
		}
		if (abs(c[0] - x) < 1e-9 && abs(c[1] - x) < 1e-9) {
			double ans = v / (r[0] + r[1]);
			printf("%.9f\n", ans);
			return ;
		}
		double v0 = v * (x - c[1]) / (c[0] - c[1]), v1 = v - v0;
		double ans = max(v0/r[0], v1/r[1]);
		printf("%.9f\n", ans);
	}
}

int main() {
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) solve(i + 1);
	return 0;
}