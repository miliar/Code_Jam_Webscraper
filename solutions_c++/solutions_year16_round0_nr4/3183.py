#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);

	int t, k, c, s;
	cin >> t;
	for (int cs = 1; cs <= t; ++cs) {
		cin >> k >> c >> s;
		cout << "Case #" << cs << ":";
		if (c == 1 && k != s or s < (k + 1) / 2)
			cout << " IMPOSSIBLE\n";
		else if (s == k) {
			for (int i = 1; i <= k; ++i)
				cout << ' ' << i;
			cout << '\n';
		} else {
			int curr = 2;
			while (curr <= k * k) {
				cout << ' ' << curr;
				curr += 2 * k + 2;
				curr -= curr == k * k + 1;
			}
			cout << '\n';
		}
	}
	return 0;
}
