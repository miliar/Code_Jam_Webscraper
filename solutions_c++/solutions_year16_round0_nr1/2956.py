#include <bits/stdc++.h>

#define ll long long
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define ld double

using namespace std;

ll n;

void add(ll n, set<int> &x) {
	while (n) {
		x.insert(n % 10);
		n /= 10ll;
	}
}

void solve(int test) {
	cout << "Case #" << test << ": ";
	cin >> n;
	if (n == 0) {
		cout << "INSOMNIA\n";
		return;
	}
	set<int> x;
	for (ll i = n; ; i += n) {
		add(i, x);
		bool kt = 1;
		for (int i = 0; i <= 9; ++i) {
			if (x.count(i) == 0) {
				kt = 0;
				break;
			}
		}
		if (kt) {
			cout << i << "\n";
			break;
		}
	}
}

int main() {
#ifdef LOCAL
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
		solve(i);
}
