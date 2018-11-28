#include <bits/stdc++.h>
#define endl "\n"
#define f first
#define s second

using namespace std;

typedef long long ll;

int main() {
	//ios::sync_with_stdio(false);

	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int t, ans;
	char cor, incor;
	string s;

	cin >> t;

	for (int i = 0; i < t; ++i) {
		cin >> s;

		ans = 0;
		cor = '+';
		incor = '-';

		for (int j = s.length() - 1; j >= 0; --j) {
			if (s[j] == cor) {
				continue;
			}

			ans++;
			for (int k = j; k >= 0; --k) {
				if (s[k] == cor) {
					j = k + 1;
					swap(cor, incor);
					break;
				}

				if (k == 0) {
					j = 0;
				}
			}
		}


		cout << "Case #" << i + 1 << ": " << ans << endl;
	}

	return 0;
}
