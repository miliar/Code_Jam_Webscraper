#include <bits/stdc++.h>
using namespace std;

string rps = "RPS";

string dfs(int d, int k) {
	if (d == 0) return string(1, rps[k]);
	string l = dfs(d - 1, k);
	string r = dfs(d - 1, (k + 1) % 3);
	if (l > r) swap(l, r);
	return l + r;
}

void solve() {
	int n;
	cin >> n;

	int a[3];
	for (int i = 0; i < 3; i++) cin >> a[i];

	string s[3];
	for (int i = 0; i < 3; i++) s[i] = dfs(n, i);

	for (int i = 0; i < 3; i++) {
		int num[3];
		for (int j = 0; j < 3; j++) {
			num[j] = count(s[i].begin(), s[i].end(), rps[j]);
		}
		bool ok = true;
		for (int j = 0; j < 3; j++) {
			if (num[j] != a[j]) ok = false;
		}
		if (ok) {
			cout << s[i] << endl;
			return;
		}
	}
	cout << "IMPOSSIBLE" << endl;
}

int main() {
	int T;
	cin >> T;

	for (int i = 0; i < T; i++) {
		printf("Case #%d: ", i + 1);
		solve();
	}
}