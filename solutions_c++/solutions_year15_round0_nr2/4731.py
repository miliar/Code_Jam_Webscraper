#include <cstdio>

int compute(int D, int* P) {
	int max_p = 0;
	for (int i = 0; i < D; ++ i)
		if (P[i] > max_p) max_p = P[i];
	int res = max_p;
	for (int k = 1; k <= max_p && k < res; ++ k) {
		int cost = k;
		for (int i = 0; i < D; ++ i) {
			cost += (P[i] - 1) / k;
			if (cost >= res) break;
		}
		if (cost < res) res = cost;
	}
	return res;
}

int main() {
	int T, D, res;
	int P[1010];

	scanf("%d", &T);
	for (int ncase = 1; ncase <= T; ++ ncase) {
		scanf("%d", &D);
		for (int i = 0; i < D; ++ i)
			scanf("%d", &P[i]);
		res = compute(D, P);
		printf("Case #%d: %d\n", ncase, res);
	}
	return 0;
}
