#include <bits/stdc++.h>

#define ll long long
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define ld double

using namespace std;

int k, c, s;

ll f(ll i) {
	return i;
}

void solve(int test) {
	cout << "Case #" << test << ": ";
	cin >> k >> c >> s;
	for (int i = 1; i < k; ++i) {
		cout << f(i) << " ";
	}
	cout << f(k) << "\n";
}

int main() {
#ifdef LOCAL
//	freopen("input.txt", "r", stdin);
	freopen("D-small-attempt2.in", "r", stdin);
	freopen("output2.txt", "w", stdout);
#endif
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
		solve(i);
}
