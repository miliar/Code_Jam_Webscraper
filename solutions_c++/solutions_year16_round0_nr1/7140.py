#include <bits/stdc++.h>
#define endl "\n"
#define f first
#define s second

using namespace std;

typedef long long ll;

int main() {
	//ios::sync_with_stdio(false);

	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	ll n, p;

	cin >> t;

	for (int i = 0; i < t; ++i) {
		cin >> n;

		if (n == 0) {
			cout << "Case #" << i + 1 << ": INSOMNIA" << endl;
			continue;
		}

		ll z = 0;

		for (int j = 1; j <= 100000; ++j) {
			p = n * j;

			while (p > 9) {
				z |= (1 << (p % 10));
				p /= 10;
			}

			z |= (1 << p);

			if (z == (1 << 10) - 1) {
				cout << "Case #" << i + 1 << ": " << n * j << endl;
				break;
			}
		}


	}

	return 0;
}
