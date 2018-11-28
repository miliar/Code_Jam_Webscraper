#include <algorithm>
#include <iomanip>
#include <iostream>
#include <cstring>
#include <sstream>
#include <vector>
#include <cmath>
#include <set>
#include <map>

using namespace std;

#define int long long
#define double long double

#define ff first
#define ss second
#define mp make_pair
#define sqr(x) ((x)*(x))

typedef long long ll;
typedef pair <int, int> pie;

const int maxN = 40;

int b, n, a[maxN];

double solve() {
	memset (a, 0, sizeof a);
	cin >> b >> n;
	for (int i = 0; i < n; i++) cin >> a[i];
	sort (a, a + 37);
	double best = 0;
	for (int i = 1, s = 0; i < 37; i++) {
		s += a[i - 1];
		int xl = min (a[i] - 1, (b + s) / i);
		for (int x = max (a[i - 1], xl - 1); x <= xl; x++) {
			int need = (i * x - s);
			for (int k = 0, S = s; k < i; k++, S -= a[i - k]) {
				if (need + k > b) continue;
				best = max (best, (double)(36 * ((i - k) * x - S)) / (i - k) - (need + k));
			}
		}
	}
	return best;
}

main() {
	ios::sync_with_stdio (false);
	
	cout << fixed << setprecision (10);
	int tests; cin >> tests;
	for (int o = 1; o <= tests; o++) {
		double ans = solve();
		cout << "Case #" << o << ": " << ans << endl;
	}

	return 0;
}
