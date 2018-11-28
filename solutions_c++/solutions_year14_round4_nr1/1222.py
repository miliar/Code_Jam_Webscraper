#include <bits/stdc++.h>

using namespace std;

#define int long long

#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define sqr(x) ((x)*(x))

typedef long long ll;
typedef pair <int, int> pie;

const int maxN = 10000;

int n, x, a[maxN];

int solve() {
	cin >> n >> x;
	for (int i = 0; i < n; i++) cin >> a[i];
	sort (a, a + n);

	int pnt = 0;
	for (int i = n - 1; i >= 0; i--) {
		if (i <= pnt) break;
		if (a[i] + a[pnt] <= x) pnt++;
	}
	return n - pnt;
}

main() {
	ios::sync_with_stdio (false);

	int tests; cin >> tests;
	for (int o = 1; o <= tests; o++) {
		int res = solve();
		cout << "Case #" << o << ": " << res << endl; 
	}

	return 0;
}
