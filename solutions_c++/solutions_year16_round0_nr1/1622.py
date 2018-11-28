#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()

const double EPS = 1e-9;
const ll INF = 1e17;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(nullptr);
	cout.tie(nullptr);

	freopen("file.in", "r", stdin);
	freopen("file.out", "w", stdout);

	int t;
	cin >> t;

	for (int i = 0; i < t; i++) {
		int n;
		cin >> n;

		if (!n) {
			cout << "Case #" << i + 1 << ": INSOMNIA\n";
			continue;
		}

		int cnt = 0, mul;
		vector<bool> was(10, 0);

		for (mul = 1; cnt < 10; mul++) {
			ll now = mul * n;

			while (now) {
				cnt += 1 - was[now % 10];
				was[now % 10] = 1;
				now /= 10;
			}

			if (mul == 1e6) {
				cerr << "Smth going wrong\n";
			}

			if (mul == 1e8) {
				cerr << "Very bad num is " << n << "\n";
			}
		}

		cout << "Case #" << i + 1 << ": " << (ll)n * (ll)(mul - 1) << "\n";
	}

	return 0;
}
