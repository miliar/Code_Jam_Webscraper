#include <bits/stdc++.h>

using namespace std;

#define MAXN 105

int di[] = { 0, 1, 0, -1 };
int dj[] = { 1, 0, -1, 0 };
int T, N, M;
string A[MAXN];

int getDir(char c) {
	if (c == '>') {
		return 0;
	} else if (c == 'v') {
		return 1;
	} else if (c == '<') {
		return 2;
	} 
	return 3;
}

bool canWalkToEdge(int pi, int pj, int d) {
	do {
		pi += di[d];
		pj += dj[d];
	} while (pi >= 0 && pi < N && pj >= 0 && pj < M && A[pi][pj] == '.');
	return !(pi >= 0 && pi < N && pj >= 0 && pj < M);
}

bool canFix(int pi, int pj) {
	for (int d = 0; d < 4; d++) {
		if (!canWalkToEdge(pi, pj, d)) {
			return true;
		}
	}
	return false;
}

int solve() {
	int ans = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (A[i][j] != '.') {
				int d = getDir(A[i][j]);
				if (canWalkToEdge(i, j, d)) {
					ans++;
					if (!canFix(i, j)) {
						return -1;
					}
				}
			}
		}
	}
	return ans;
}

int main() {
	freopen("date.in", "r", stdin);
	freopen("date.out","w", stdout);
	cin.sync_with_stdio(false);
	
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> N >> M;
		for (int i = 0; i < N; i++) {
			cin >> A[i];
		}
		int ans = solve();
		cout << "Case #" << t << ": ";
		if (ans == -1) {
			cout << "IMPOSSIBLE\n";
		} else {
			cout << ans << '\n';
		}
	}
	
	return 0;
}
