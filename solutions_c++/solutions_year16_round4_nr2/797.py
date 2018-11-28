#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
#define size(x) (int) x.size()
#define sqr(x) ((x) * (x))

const int maxn = 20;
const int logn = 18;
const int inf = (int) 1e9 + 5;
const long long mod = (int) 1e9 + 7;
const long long base = 2204234849;
const long long l_inf = (long long) 4e18;
const long double pi = acos(-1.0);
const long double eps = 1e-12;

int n, k;
long double p[maxn];
long double Yes[1 << maxn], No[1 << maxn];
int cnt[1 << maxn];


inline long double solve() {
	for (int mask = 0; mask < (1 << n); mask++) {
		Yes[mask] = No[mask] = 1.0;
		cnt[mask] = 0;
		for (int i = 0; i < n; i++) {
			if (mask & (1 << i)) {
				Yes[mask] *= p[i];
				No[mask] *= 1.0 - p[i];
				cnt[mask]++;
			}
		}
	}

	long double best = 0.0;
	for (int mask = 0; mask < (1 << n); mask++) {
		if (cnt[mask] != k)
			continue;
		long double ans = 0.0;
		for (int mask2 = mask; mask2 > 0; mask2 = (mask2 - 1) & mask) {
			if (cnt[mask2] * 2 != k)
				continue;
			ans += Yes[mask2] * No[mask ^ mask2];
		}
		best = max(best, ans);
	}
	return min((long double) 1.0, best);
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.precision(20);
	cout << fixed;
	srand(566);

	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> n >> k;
		for (int i = 0; i < n; i++)
			cin >> p[i];

		cout << "Case #" << t << ": ";
		cout << solve();
		cout << '\n';
	}

	return 0;
}
