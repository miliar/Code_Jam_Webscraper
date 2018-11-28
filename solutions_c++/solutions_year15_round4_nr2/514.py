#include<iostream>
#include<cstdio>
using namespace std;
#define MAXN 100
double r[MAXN], c[MAXN];
int main() {
	int T;
	int ca = 1;
	freopen("in", "r", stdin);
	freopen("r2", "w", stdout);
	cin >> T;
	while (T--) {
		int n;
		double V, X;
		cin >> n >> V >> X;
		for (int i = 0; i < n; i++) {
			cin >> r[i] >> c[i];
		}
		printf("Case #%d: ", ca++);
		if (n == 1) {
			if (X == c[0]) {
				printf("%.8lf\n", V / r[0]);
			} else {
				puts("IMPOSSIBLE");
			}
		} else {
			if (c[0] == c[1]) {
				if (c[0] == X) {
					printf("%.8lf\n", V / (r[0] + r[1]));
				} else {
					puts("IMPOSSIBLE");
				}
			} else {
				double x = V * (X - c[1]) / (c[0] - c[1]);
				double y = V - x;
				if (x >= 0 && y >= 0 && x <= V && y <= V) {
					printf("%.8lf\n", max(x / r[0], y / r[1]));
				} else if (c[0] == X) {
					printf("%.8lf\n", V / r[0]);
				} else if (c[1] == X) {
					printf("%.8lf\n", V / r[1]);
				} else {
					puts("IMPOSSIBLE");
				}
			}
		}
	}
	return 0;
}
/**
 6
 1 10.0000 50.0000
 0.2000 50.0000
 2 30.0000 65.4321
 0.0001 50.0000
 100.0000 99.9000
 2 5.0000 99.9000
 30.0000 99.8999
 20.0000 99.7000
 2 0.0001 77.2831
 0.0001 97.3911
 0.0001 57.1751
 2 100.0000 75.6127
 70.0263 75.6127
 27.0364 27.7990
 */
