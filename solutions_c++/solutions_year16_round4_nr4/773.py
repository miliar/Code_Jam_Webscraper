#include <bits/stdc++.h>

using namespace std;

#define MAXN 5

int N;
string A[MAXN];
int B[MAXN];
int ANS;
int P[MAXN];
bool dp[MAXN][1 << MAXN];

bool canWork() {
	memset(dp, 0, sizeof(dp));

	dp[0][0] = true;
	for (int i = 0; i < N; i++) {
		int p = P[i];
		bool ok = true;
		for (int mask = 0; mask < (1 << N); mask++) {
			if (dp[i][mask]) {
				bool can = false;
				for (int j = 0; j < N; j++) {
					if ((B[p] & (1 << j)) > 0 && (mask & (1 << j)) == 0) {
						can = true;
						int nmask = mask | (1 << j);
						dp[i + 1][nmask] = true;
					}
				}
				if (!can) {
					ok = false;
				}
			}
		}

		if (!ok) {
			return false;
		}
	}

	return true;
}

int transf(string &s) {
	int ret = 0;
	for (int i = 0; i < N; i++) {
		if (s[i] == '1') {
			ret |= 1 << i;
		}
	}
	return ret;
}

void check(int c) {
	for (int i = 0; i < N; i++) {
		P[i] = i;
	}

	for (int i = 0; i < N; i++) {
		B[i] = transf(A[i]);
	}

	do {
		if (!canWork()) {
			return;
		}
	} while (next_permutation(P, P + N));

	ANS = min(ANS, c);
}

void go(int pi, int pj, int c) {
	if (pi == N) {
		check(c);
		return;
	}

	int ni = pi;
	int nj = pj + 1;
	if (nj == N) {
		ni++;
		nj = 0;
	}
	go(ni, nj, c);

	if (A[pi][pj] == '0') {
		A[pi][pj] = '1';
		go(ni, nj, c + 1);
		A[pi][pj] = '0';
	}
}

int solve() {
	ANS = N * N;
	go(0, 0, 0);
	return ANS;
}

int main() {
	assert(freopen("D.in", "r", stdin));
	assert(freopen("D.out", "w", stdout));
	cin.sync_with_stdio(false);

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";

		cin >> N;
		for (int i = 0; i < N; i++) {
			cin >> A[i];
		}

		int ans = solve();
		cout << ans << '\n';
		
		cerr << t << endl;
	}

	return 0;
}
