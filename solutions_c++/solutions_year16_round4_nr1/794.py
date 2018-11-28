#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
#define size(x) (int) x.size()
#define sqr(x) ((x) * (x))

const int maxn = 100005;
const int logn = 18;
const int inf = (int) 1e9 + 5;
const long long mod = (int) 1e9 + 7;
const long long base = 2204234849;
const long long l_inf = (long long) 4e18;
const long double pi = acos(-1.0);
const long double eps = 1e-12;

int N, R, P, S;
string ans;

string get(int l, int r) {
	if (r - l == 1)
		return ans.substr(l, 1);
	string x = get(l, (l + r) >> 1);
	string y = get((l + r) >> 1, r);
	return min(x + y, y + x);
}


string Try(int lvl, int r, int p, int s) {
	if (lvl == N) {
		if (r == R && p == P && s == S) {
			return get(0, 1 << N);
		}
		return "IMPOSSIBLE";
	}
	for (int i = 0; i < (1 << N); i += 1 << (N - lvl)) {
		if (ans[i] == 'R') {
			ans[i + (1 << (N - lvl - 1))] = 'S';
			s++;
		}
		if (ans[i] == 'P') {
			ans[i + (1 << (N - lvl - 1))] = 'R';
			r++;
		}
		if (ans[i] == 'S') {
			ans[i + (1 << (N - lvl - 1))] = 'S';
			ans[i] = 'P';
			p++;
		}
	}
	return Try(lvl + 1, r, p, s);
}

inline void solve() {
	ans.resize(1 << N);
	ans[0] = 'R';
	string x = Try(0, 1, 0, 0);
	ans[0] = 'P';
	string y = Try(0, 0, 1, 0);
	ans[0] = 'S';
	string z = Try(0, 0, 0, 1);
	if (x == y && y == z) {
		cout << "IMPOSSIBLE";
	} else {
		string best = "ZZZ";
		if (x != "IMPOSSIBLE")
			best = min(best, x);
		if (y != "IMPOSSIBLE")
			best = min(best, y);
		if (z != "IMPOSSIBLE")
			best = min(best, z);
		cout << best;
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.precision(10);
	cout << fixed;
	srand(566);

	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> N >> R >> P >> S;
		cout << "Case #" << t << ": ";
		solve();
		cout << '\n';
	}

	return 0;
}
