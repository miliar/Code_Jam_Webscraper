#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

#define all_of(v) v.begin(), v.end()
#define fi first
#define se second
#define pb push_back

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);

	int t;
	cin >> t;

	for (int test = 1; test <= t; test++) {
		int a, b, k;
		cin >> a >> b >> k;

		int ans = 0;

		for (int i = 0; i < a; i++) {
			for (int j = 0; j < b; j++) {
				if ((i & j) < k) {
					ans++;
				}
			}
		}

		cout << "Case #" << test << ": " << ans << endl;
	}
}