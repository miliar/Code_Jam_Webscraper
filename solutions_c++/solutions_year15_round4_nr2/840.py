#include"stdio.h"
#include"stdlib.h"
#include"algorithm"
using namespace std;
typedef long long LL;
typedef pair<int, int> II;
int t, T, N;
double V, X, R[105], C[105], EPS = 1e-9;
int main() {
	freopen("B-small-attempt2.in", "r", stdin);
	freopen("B-small-attempt2.txt", "w", stdout);
	scanf("%d", &T);
	while (t < T) {
		scanf("%d%lf%lf", &N, &V, &X);
		for (int i = 0; i < N; i++)
			scanf("%lf%lf", &R[i], &C[i]);
		if (N == 1) {
			if (X != C[0])
				printf("Case #%d: IMPOSSIBLE\n", ++t);
			else 
				printf("Case #%d: %lf\n", ++t, V / R[0]);
			continue;
		}
		double C0 = C[0] - X, C1 = C[1] - X;
		if (fabs(C0) < EPS) {
			if (fabs(C1) < EPS) R[0] += R[1];
			printf("Case #%d: %lf\n", ++t, V / R[0]);
			continue;
		}
		if (fabs(C1) < EPS) {
			printf("Case #%d: %lf\n", ++t, V / R[1]);
			continue;
		}
		double V0 = V / (C[0] - C[1]) * (X - C[1]) ;
		double V1 = V - V0;
		if (V0 < EPS || V1 < EPS)  {
			printf("Case #%d: IMPOSSIBLE\n", ++t);
			continue;
		}
		double TS = max(V0 / R[0], V1 / R[1]);
		printf("Case #%d: %.9lf\n", ++t, TS);
	}
}
/*
1
2 99.4808 76.9326
99.9999 76.9326
100.0000 76.9326
*/
