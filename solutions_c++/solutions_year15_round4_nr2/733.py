#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
	int T;
	scanf("%d", &T);

	int i;

	for (i = 0; i < T; ++i) {
		int N;

		scanf("%d", &N);

		double V, X;

		scanf("%lf %lf", &V, &X);

		int j;
		double R[102];
		double C[102];

		double R0 = 0;
		double R1 = 0;
		double R2 = 0;

		double C0 = 0;
		double C1 = 0;
		double C2 = 0;

		for (j = 0; j < N; ++j) {
			scanf("%lf %lf", &R[j], &C[j]);

			if (fabs(X - C[j]) < 0.00000001) {
				R1 += R[j];
				C1 += R[j] * C[j];
			} else if (C[j] < X) {
				R0 += R[j];
				C0 += R[j] * C[j];
			} else {
				R2 += R[j];
				C2 += R[j] * C[j];
			}
		}

		if ((fabs(R0) < 0.00000001 && fabs(R1) < 0.00000001) ||
			(fabs(R1) < 0.00000001 && fabs(R2) < 0.00000001)) {

				printf("Case #%d: IMPOSSIBLE\n", i + 1);
				continue;
		}

		if (fabs(R0) < 0.00000001 || fabs(R2) < 0.00000001) {
			printf("Case #%d: %.9lf\n", i + 1, V / R1);
			continue;
		}

		C0 /= R0;
		C2 /= R2;

		double gap0 = X - C0;
		double gap2 = C2 - X;

		double time0 = gap2 / R0;
		double time2 = gap0 / R2;
		double time1 = max(time0, time2);

		time0 /= time1;
		time2 /= time1;

		double allV = time0 * R0 + time1 * R1 + time2 * R2;
		double goodtime = V / allV;

		printf("Case #%d: %.9lf\n", i + 1, goodtime);
	}
}