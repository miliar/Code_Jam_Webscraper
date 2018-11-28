#include <bits/stdc++.h>

#define ll long long
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define ld double

using namespace std;

int n, m;

ll uoc(ll n) {
	if (n < 4)
		return -1;
	if (n % 2 == 0)
		return 2;
	for (ll i = 3; i * i <= n; i += 2)
		if (n % i == 0)
			return i;
	return -1;
}

bool ok(int n, string &bin, vector<int> &res) {
	bin = "";
	while (n) {
		bin = char(n % 2 + 48) + bin;
		n /= 2;
	}
	res.clear();
	for (int i = 2; i <= 10; ++i) {
		ll tmp = 0;
		for (int j = 0; j < bin.length(); ++j) {
			tmp = tmp * (ll) i + (ll) (bin[j] - 48);
		}
		ll tmp2 = uoc(tmp);
		if (tmp2 == -1)
			return 0;
		res.pb(tmp2);
	}
	return 1;
}

void solve(int test) {
	cout << "Case #" << test << ":\n";
	cin >> n >> m;
	vector<int> tmp;
	string bin;
	for (int i = (1 << (n - 1)) + 1; i < (1 << n) && m; i += 2) {
		if (ok(i, bin, tmp)) {
			cout << bin << " ";
			for (int i = 0; i + 1 < tmp.size(); ++i) {
				cout << tmp[i] << " ";
			}
			cout << tmp.back() << "\n";
			m--;
		}
	}
}

int main() {
#ifdef LOCAL
//	freopen("input.txt", "r", stdin);
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("output2.txt", "w", stdout);
#endif
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
		solve(i);
}
