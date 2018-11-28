#include <cstdio>
#include <iostream>
using namespace std;

const int MAXN = 18;
int N, K;
double P[MAXN], f[1 << MAXN][MAXN];

int lowbit(int x) {
	return (x & (x ^ (x - 1)));
}

int pow2int(int x) {
	int ans = 0;
	while (x > 1) x >>= 1, ++ans;
	return ans;
}

int count1(int x) {
	int ans = 0;
	while (x) {
		ans += (x & 1);
		x >>= 1;
	}
	return ans;
}

double DP() {
	double ans = 0;
	f[0][0] = 1;
	for (int k = 1; k <= K; ++k)
		f[0][k] = 0;
	for (int S = 1; S < (1 << N); ++S) {
		if (count1(S) > K) continue;
		for (int k = 0; k <= K; ++k) {
			int x = lowbit(S);
			int id = pow2int(x);
			f[S][k] = f[S - x][k] * (1 - P[id]);
			if (k > 0) f[S][k] += f[S - x][k - 1] * P[id];
		}
		if (count1(S) == K)
			ans = max(ans, f[S][K >> 1]);
	}
	return ans;
}

int main() {
	FILE *ifp = fopen("B-small-attempt0.in", "r");
	FILE *ofp = fopen("B.out", "w");
	int T;
	fscanf(ifp, "%d", &T);
	for (int t = 1; t <= T; ++t) {
		fscanf(ifp, "%d%d", &N, &K);
		for (int i = 0; i < N; ++i)
			fscanf(ifp, "%lf", &P[i]);
		fprintf(ofp, "Case #%d: %.6f\n", t, DP());
	}
	fclose(ifp);
	fclose(ofp);
	return 0;
}
