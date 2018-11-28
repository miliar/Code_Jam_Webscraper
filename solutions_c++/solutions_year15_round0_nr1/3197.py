#include <bits/stdc++.h>

using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int test;
	cin >> test;
	for (int t = 1; t <= test; t++) {
		int n;
		string s;
		cin >> n >> s;
		int res = 0;
		int sum = s[0] - 48;
		for (int i = 1; i <= n; i++) {
			if (s[i] > 48) {
				res += max(0, i - sum);
				sum += max(0, i - sum);
				sum += s[i] - 48;
			}
		}
		cout << "Case #" << t << ": " << res << "\n";
	}
}