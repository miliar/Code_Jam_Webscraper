#include "bits/stdc++.h"

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	freopen("in", "rt", stdin);
	freopen("out", "wt", stdout);
	int T;
	cin >> T;

	for (int t = 1; t <= T; ++t) {
		int n = 0, cnt = 0, res = 0;
		char tmp;
		cin >> n;

		for (int i = 0; i <= n; ++i) {
			cin >> tmp;
			if (tmp == '0')
				continue;

			if (cnt < i) {
				res += (i - cnt);
				cnt += (i - cnt);
			}
			cnt += (tmp - '0');
		}

		cout << "Case #" << t << ": " << res << endl;

	}
	return 0;
}
