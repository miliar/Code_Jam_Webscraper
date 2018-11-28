#include <cstdio>
#include <algorithm>
#include <iostream>
using namespace std;

int N;
char s[10][10];
bool f[5][1 << 16];

int count1(int x) {
	int ans = 0;
	while (x) {
		ans += (x & 1);
		x >>= 1;
	}
	return ans;
}

int cancel(int S, int id, int k) {
	int a[5][5];
	for (int i = 0; i < k; ++i) {
		for (int j = 0; j < k; ++j) {
			a[i][j] = (S >> (i * k + j)) & 1;
		}
	}
	int cnt = 0, ans = 0;
	int x = id / k, y = id % k;
	for (int i = 0; i < k; ++i) {
		for (int j = 0; j < k; ++j) {
			if (i != x && j != y) {
				ans += (a[i][j] << (cnt++));
			}
		}
	}
	return ans;
}

void preprocess() {
	f[1][0] = false; f[1][1] = true;
	for (int k = 2; k <= 4; ++k) {
		f[k][0] = false;
		for (int S = 1; S < (1 << (k * k)); ++S) {
			f[k][S] = true;
			for (int i = 0; i < k * k; ++i)
				if (((S >> i) & 1) && !f[k - 1][cancel(S, i, k)]) {
					f[k][S] = false;
					break;
				}
		}
	}
}

int findAns() {
	int S = 0, ans = 100;
	for (int i = 0; i < N; ++i)
		for (int j = 0; j < N; ++j)
			S += (s[i][j] << (i * N + j));
	for (int T = 0; T < (1 << (N * N)); ++T) {
		if ((T | S) == T && f[N][T])
			cout << T << "!\n",
			ans = min(ans, count1(T - S));
	}
	return ans;
}

int main() {
	FILE *ifp = fopen("D-small-attempt0.in", "r");
	FILE *ofp = fopen("D.out", "w");
	int T;
	fscanf(ifp, "%d", &T);
	preprocess();
	for (int t = 1; t <= T; ++t) {
		fscanf(ifp, "%d", &N);
		for (int i = 0; i < N; ++i) {
			fscanf(ifp, " %s", s[i]);
			for (int j = 0; j < N; ++j)
				s[i][j] -= '0';
		}
		fprintf(ofp, "Case #%d: %d\n", t, findAns());
	}
	fclose(ifp);
	fclose(ofp);
	return 0;
}
