#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>

using namespace std;

const int N_MAX = 2;

void print_result(int t, double result) {
	if (result == -1) {
		printf("Case #%d: IMPOSSIBLE\n", t);
	} else {
		printf("Case #%d: %.6lf\n", t, result);
	}
}

double V[N_MAX];
double X[N_MAX];

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		double result = 0;
		int N;
		double v, x;
		scanf("%d %lf %lf", &N, &v, &x);
		for (int i = 0; i < N; ++i) {
			scanf("%lf %lf", &V[i], &X[i]);
		}
		if (N == 1) {
			V[1] = 0;
			X[1] = X[0];
		}
		if (x > fmax(X[0], X[1]) || x < fmin(X[0], X[1])) {
			result = -1;
		} else {
			if (X[0] == X[1]) {
				V[0] += V[1];
				--N;
				result = v / V[0];
			} else {
				double v_prim = (double)(x - X[1]) / (double)(X[0] - X[1]) * v;
				double v_prim2 = v - v_prim;
				result = fmax(v_prim / V[0], v_prim2 / V[1]);
			}
		}
		print_result(t, result);
	}
	return 0;
}