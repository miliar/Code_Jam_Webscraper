#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()

const double EPS = 1e-9;
const ll INF = 1e17;

string orig;

void print(bool type, int deep) {
	if (!deep && !type) {
		cout << orig;
	} else if (!deep && type) {
		for (int i = 0; i < (int)orig.size(); i++) {
			cout << "G";
		}
	}

	if (!deep) return;

	for (int i = 0; i < (int)orig.size(); i++) {
		print(orig[i] == 'G', deep - 1);
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(nullptr);
	cout.tie(nullptr);

	freopen("file.in", "r", stdin);
	freopen("file.out", "w", stdout);

	int t;
	cin >> t;

	for (int testNum = 1; testNum <= t; testNum++) {
		cout << "Case #" << testNum << ": ";

		int k, c, s;
		cin >> k >> c >> s;

		if (c == 1) {
			if (s < k) {
				cout << "IMPOSSIBLE\n";
				continue;
			}

			for (int i = 1; i <= s; i++) {
				cout << i << " ";
			}
			cout << "\n";
		} else {
			if (k / 2 + (k % 2) > s) {
				cout << "IMPOSSIBLE\n";
				continue;
			}

			for (int step = 1; step * k + step <= k * k; step += 2) {
				cout << step * k + step << " ";
			}

			if (k % 2) {
				cout << k << " ";
			}
			cout << "\n";
		}
	}

	// int n, d;
	// cin >> n >> d;

	// for (int i = 0; i < (1 << n); i++) {
	// 	orig.clear();

	// 	for (int j = 0; j < n; j++) {
	// 		orig.push_back(((i >> j) & 1) ? 'G' : 'L');
	// 	}

	// 	print(0, d - 1);
	// 	cout << "\n";
	// }

	return 0;
}
