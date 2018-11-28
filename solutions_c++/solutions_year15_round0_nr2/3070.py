#include <bits/stdc++.h>

using namespace std;

int n;
int res;
int a[1005];

int check(int f) {
	for (int s = 0; s < f; s++) {
		int sum = 0;
		for (int i = 0; i < n; i++) {
			if (a[i] + s > f) {
				int x = f - s;
				sum += (a[i] - 1) / x;
			}
		}
		if (sum <= s) {
			return 1;
		}
	}
	return 0;
}

int solve() {
	int l = 0;
	int r = 1005;
	while (r - l > 1) {
		int mid = (l + r) >> 1;
		if (check(mid)) {
			r = mid;
		} else {
			l = mid;
		}
	}
	res = r;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int T;
	cin >> T;
	for (int test = 1; test <= T; test++) {
		cin >> n;
		for (int i = 0; i < n; i++)	{
			cin >> a[i];
		}
		solve();
		cout << "Case #" << test << ": " << res << "\n";
	}
}