#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

int N, K;
vector<double> P;

double solve() {
	sort(P.begin(), P.end());
	double sol = 0.0;
	for (int i = 1; i < (1 << N); ++i) {
		if (__builtin_popcount(i) != K)
			continue;
		int kk = 0;
		vector<double> Q(K);
		for (int j = 0; j < N; ++j) {
			if (i & (1 << j)) {
				Q[kk++] = P[j];
			}
		}

		double p = 0.0;
		for (int j = 1; j < (1 << K); ++j) {
			if (__builtin_popcount(j) * 2 != K)
				continue;
			double pp = 1.0;
			for (int k = 0; k < K; ++k) {
				if (j & (1 << k)) {
					pp *= Q[k];
				} else {
					pp *= (1 - Q[k]);
				}
			}
			p += pp;
		}

		sol = max(sol, p);
	}
	return sol;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d%d", &N, &K);
		P.resize(N);
		for (int i = 0; i < N; ++i) {
			cin >> P[i];
		}
		cout << "Case #" << t << ": " << solve() << endl;
	}
	return 0;
}
