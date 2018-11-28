#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
#define size(x) (int) x.size()
#define sqr(x) ((x) * (x))

const int maxn = 205;
const int logn = 18;
const int inf = (int) 1e9 + 5;
const long long mod = (int) 1e9 + 7;
const long long base = 2204234849;
const long long l_inf = (long long) 4e18;
const long double pi = acos(-1.0);
const long double eps = 1e-12;

int n;
int g[maxn];
int machine[maxn];
int worker[maxn];
int ans;

inline bool can() {
	for (int i = 0; i < n; i++) {
		machine[i] = 0;
		worker[i] |= g[i];
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (worker[i] & (1 << j))
				machine[j] |= 1 << i;
		}
	}

	for (int i = 0; i < n; i++)
		if (machine[i] == 0 || worker[i] == 0)
			return false;

	for (int i = 0; i < n; i++) {
		int mask = 0, cnt1 = 0, cnt2 = 0;
		for (int j = 0; j < n; j++) {
			if (worker[i] & (1 << j)) {
				mask |= machine[j];
				cnt1++;
			}
		}
		for (int j = 0; j < n; j++) {
			if (mask & (1 << j))
				cnt2++;
		}
		if (cnt2 > cnt1)
			return false;
	}
	return true;
}

inline int get() {
	int sum = 0;
	for (int i = 0; i < n; i++) {
		int mask = worker[i] ^ g[i];
		int cnt = 0;
		for (int j = 0; j < n; j++)
			if (mask & (1 << j))
				cnt++;
		sum += cnt;
	}
	return sum;
}

void gen(int i) {
	if (i == n) {
		if (can())
			ans = min(ans, get());
		return;
	}
	for (int mask = 0; mask < (1 << n); mask++) {
		worker[i] = mask;
		gen(i + 1);
	}
}

inline void solve() {
	ans = inf;
	cin >> n;
	for (int i = 0; i < n; i++) {
		g[i] = 0;
		for (int j = 0; j < n; j++) {
			char x;
			cin >> x;
			if (x == '1')
				g[i] |= 1 << j;
		}
	}
	gen(0);
	cout << ans;
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
		cout << "Case #" << t << ": ";
		solve();
		cout << '\n';
	}

	return 0;
}
