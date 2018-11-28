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

const int maxN = 1000 + 10;

int n;
double a[maxN], b[maxN];

pie solve() {
	cin >> n;
	for (int i = 0; i < n; i++) cin >> a[i];
	for (int i = 0; i < n; i++) cin >> b[i];

	sort (a, a + n);
	sort (b, b + n);
	
	pie res (0, 0);

	int last = -1;
	for (int i = 0; i < n; i++) {
		int x = max (last + 1, (long long)(lower_bound (b, b + n, a[i]) - b));
		if (x >= n) { res.ss = n - i; break; }
		last = x;
	}

	last = -1; res.ff = n;
	for (int i = 0; i < n; i++) {
		int x = max (last + 1, (long long)(lower_bound (a, a + n, b[i]) - a));
		if (x >= n) { res.ff = i; break; }
		last = x;
	}

	return res;
}

main() {
	ios::sync_with_stdio (false);

	int tests; cin >> tests;
	for (int o = 1; o <= tests; o++) {
		pie res = solve();
		cout << "Case #" << o << ": " << res.ff << ' ' << res.ss << endl; 
	}

	return 0;
}
