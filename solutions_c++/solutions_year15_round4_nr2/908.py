#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cmath>
#include <algorithm>
#include <queue>
#include <vector>
#include <string>
#include <functional>
using namespace std;

int T, N;
double V, X;
double R[128], C[128];
int ans, test;
const double eps = 1e-8;

int main() {
	scanf("%d", &T);
	while (T--) {
		scanf("%d", &N);
		scanf("%lf %lf", &V, &X);

		for (int i = 0; i < N; i++) {
			scanf("%lf %lf", R + i, C + i);
		}
		printf("Case #%d: ", ++test);

		if (N == 2 && abs(C[1] - C[0]) < eps) {
			N = 1;
			R[0] = R[0] + R[1];
		}
		if (N == 1) {
			double t = V / R[0];
			if (abs(R[0] * C[0] * t - V * X) > eps) {
				puts("IMPOSSIBLE");
//				printf("%.8lf %.8lf\n", R[0], C[0]);
			}
			else printf("%.8lf\n", t);
		} else {
			double t2 = (C[0] * V - X * V) / (R[1] * C[0] - R[1] * C[1]);
			double t1 = (V - R[1] * t2) / R[0];
			if (!((C[0] >= X + eps && C[1] >= X + eps) || (C[0] <= X - eps && C[1] <= X - eps))) printf("%.8lf\n", max(t1, t2));
			else {
				puts("IMPOSSIBLE");
//				printf("%.8lf %.8lf %.8lf %.8lf\n", R[0], C[0], R[1], C[1]);
			}
		}

	}

	return 0;
}
