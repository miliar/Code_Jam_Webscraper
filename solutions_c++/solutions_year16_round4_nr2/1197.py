#include <bits/stdc++.h>

using namespace std;

#define MAXN 20

int N, K;
double P[MAXN];
double S[MAXN][MAXN][MAXN];
double C[MAXN];

double calcProb(int mask) {
	for (int p = 0; p <= K; p++) {
		for (int i = 0; i <= K; i++) {
			for (int j = 0; j <= K; j++) {
				S[p][i][j] = 0.0;
			}
		}
	}

	int idx = 0;
	for (int i = 0; i < N; i++) {
		if ((mask & (1 << i)) > 0) {
			C[idx++] = P[i];
		}
	}

	S[0][0][0] = 1.0;
	for (int p = 0; p < K; p++) {
		for (int i = 0; i < K; i++) {
			for (int j = 0; j < K; j++) {
				S[p + 1][i][j + 1] += S[p][i][j] * C[p];
				S[p + 1][i + 1][j] += S[p][i][j] * (1.0 - C[p]);
			}
		}
	}

	double ret = 0.0;
	for (int i = 0; i <= K; i++) {
		ret += S[K][i][i];
	}
	return ret;
}

double solve() {
	double ans = 0.0;
	for (int mask = 0; mask < (1 << N); mask++) {
		if (__builtin_popcount(mask) == K) {
			double prob = calcProb(mask);
			ans = max(ans, prob);
		}
	}
	return ans;
}

int main() {
	assert(freopen("B.in", "r", stdin));
	assert(freopen("B.out", "w", stdout));
	cin.sync_with_stdio(false);

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";

		cin >> N >> K;
		for (int i = 0; i < N; i++) {
			cin >> P[i];
		}

		double ans = solve();
		cout << fixed << setprecision(7) << ans << '\n';
		
		cerr << t << endl;
	}

	return 0;
}
