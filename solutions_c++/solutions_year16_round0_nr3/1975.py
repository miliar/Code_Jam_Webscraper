#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define all(x) x.begin(), x.end()
#define size(x) (int) x.size()

const int maxn = 505;
const int logn = 10;
const int inf = (int) 2e9 + 5;
const long long mod = (int) 1e9 + 7;
const long long base = 2204234849;
const long long l_inf = (long long) 4e18;
const long double pi = acos(-1.0);
const long double eps = 1e-12;

int T, n, k;
vector<int> primes;

void print(long long mask, vector<int> divs) {
	for (int i = n - 1; i >= 0; i--)
		cout << (mask & (1ll << i) ? 1 : 0);
	for (int d : divs)
		cout << ' ' << d;
	cout << '\n';
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.precision(12);
	cout << fixed;
	srand(566);

#ifdef LOCAL
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
#endif

	for (int i = 2; size(primes) < 100; i++) {
		bool good = true;
		for (int j = 2; j * j <= i; j++)
			good &= i % j != 0;
		if (good)
			primes.pb(i);
	}

	cin >> T >> n >> k;
	cout << "Case #1:\n";

	for (long long mid = 0; mid < (1ll << (n - 2)) && k > 0; mid++) {
		long long mask = (1ll << (n - 1)) | (mid << 1) | 1;
		vector<int> divs;
		for (int x = 2; x <= 10; x++) {
			bool found = false;
			for (int p : primes) {
				int m = 0;
				for (int i = 0, y = 1; (1ll << i) <= mask; i++, y = (y * x) % p) {
					if (mask & (1ll << i))
						m += y;
				}
				m %= p;
				if (m == 0) {
					divs.pb(p);
					found = true;
					break;
				}
			}
			if (!found)
				break;
		}
		if (size(divs) == 9) {
			k--;
			print(mask, divs);
		}
	}

	return 0;
}
