#include <bits/stdc++.h>

using namespace std;

string S;
int K;

int solve() {
	int N = (int) S.size();
	int ret = 0;

	for (int i = K - 1; i < N; i++) {
		if (S[i - K + 1] == '-') {
			for (int j = i - K + 1; j <= i; j++) {
				S[j] = S[j] == '+' ? '-' : '+';
			}
			ret++;
		}
	}

	bool ok = true;
	for (int i = N - K; i < N; i++) {
		if (S[i] == '-') {
			ok = false;
		}
	}

	if (!ok) {
		return -1;
	} else {
		return ret;
	}
}

int main() {
	assert(freopen("A.in", "r", stdin));
	assert(freopen("A.out", "w", stdout));
	cin.sync_with_stdio(false);

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";

		cin >> S >> K;
		int ans = solve();

		if (ans == -1) {
			cout << "IMPOSSIBLE" << endl;
		} else {
			cout << ans << endl;
		}
		
		cerr << t << endl;
	}

	return 0;
}
