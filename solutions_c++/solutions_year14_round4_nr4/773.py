#include <iostream>
#include <set>
#include <string>
using namespace std;

const int mod = 1000000007;
string s[8];

int calc(int is[], int n) {
	set<string> t;
	int i, j;

	for (i = 0; i < n; i++) for (j = 0; j <= s[is[i]].size(); j++) t.insert(string(s[is[i]], 0, j));

	return t.size();
}

int main() {
	int nt, it;

	cin >> nt;
	for (it = 1; it <= nt; it++) {
		int m, n, i, x, X = 0, Y = 0;

		cin >> m >> n;
		for (i = 0; i < m; i++) {
			cin >> s[i];
		}

		for (x = 0; x < 1 << 2 * m; x++) {
			int t[4][8], nt[4] = {};

			for (i = 0; i < m; i++) {
				int it = x >> 2 * i & 3;

				if (it >= n) break;
				t[it][nt[it]++] = i;
			}
			if (i == m) {
				int X1 = 0;

				for (i = 0; i < n; i++) X1 += calc(t[i], nt[i]);
				if (X1 > X) {
					X = X1;
					Y = 1;
				} else if (X1 == X) {
					Y = (Y + 1) % mod;
				}
			}
		}

		cout << "Case #" << it << ": " << X << ' ' << Y << endl;
	}
}
