#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

int n;
double R[105], C[105], V, X;
void solve() {
	scanf("%d%lf%lf", &n, &V, &X);
	for (int i = 0; i < n; ++i) scanf("%lf%lf", &R[i], &C[i]);
	if (n == 1) {
		if (C[0] != X)
			printf("IMPOSSIBLE\n");
		else
			printf("%f\n", V / R[0]);
		return;
	}
	if (n == 2) {
		if (C[0] > C[1]) {
			swap(C[0], C[1]);
			swap(R[0], R[1]);
		}
		if (!(C[0] <= X && X <= C[1])) {
			printf("IMPOSSIBLE\n");
			return;
		}
		if (C[0] == X && C[1] != X) {
			printf("%f\n", V / R[0]);
			return;
		}
		if (C[0] != X && C[1] == X) {
			printf("%f\n", V / R[1]);
			return;
		}
		if (C[0] == X && C[1] == X) {
			printf("%f\n", V / (R[0] + R[1]));
			return;
		}
		double v0 = (X - C[1]) / (C[0] - C[1]) * V;
		double v1 = V - v0;
		printf("%f\n", max(v0 / R[0], v1 / R[1]));
	}
}
int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	int T; scanf("%d", &T);
	for (int _ = 1; _ <= T; ++_) {
		printf("Case #%d: ", _);
		solve();
	}
	return 0;
}
