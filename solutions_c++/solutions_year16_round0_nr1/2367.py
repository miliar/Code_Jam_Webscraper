#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define all(x) x.begin(), x.end()
#define size(x) (int) x.size()

const int maxn = 505;
const int logn = 10;
const int inf = (int) 2e9 + 5;
const long long mod = (int) 1e9+7;
const long long base = 2204234849;
const long long l_inf = (long long) 4e18;
const long double pi = acos(-1.0);
const long double eps = 1e-12;

int T;
long long n;
bool used[10];

int get(long long x) {
	int cnt = 0;
	while (x != 0) {
		cnt += !used[x % 10];
		used[x % 10] = true;
		x /= 10;
	}
	return cnt;
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

	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> n;

		int cnt = 0;
		memset(used, false, sizeof used);
		bool found = false;

		cout << "Case #" << t << ": ";
		for (int i = 1; i <= 100000; i++) {
			cnt += get(i * n);
			if (cnt == 10) {
				cout << i * n << '\n';
				found = true;
				break;
			}
		}
		if (!found)
			cout << "INSOMNIA\n";
	}

	return 0;
}
