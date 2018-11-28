#include <bits/stdc++.h>
using namespace std;

const int
	MAXN = 1005;

int T, N;
int a[MAXN];

int main() {

	cin >> T;
	for (int test = 1; test <= T; ++test) {

		cin >> N;
		for (int i = 0; i < N; ++i)
			cin >> a[i];

		int ans = 1000000;
		for (int x = 1; x <= 1000; ++x) {
			int t = x;
			for (int i = 0; i < N; ++i)
				t += (a[i]-1) / x;
			ans = min(ans, t);
		}

		cout << "Case #" << test << ": " << ans << endl;
	}

	return 0;
}
