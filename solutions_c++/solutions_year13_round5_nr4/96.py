#include <algorithm>
#include <iostream>
#include <cstring>
#include <sstream>
#include <iomanip>
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

const int maxN = 20 + 1;

int n;
double d[1 << maxN];

double find (int mask) {
	double &res = d[mask];
	if (res > -0.5) return res;
	if (mask == (1 << n) - 1) return res = 0;
	double ans = 0;
	for (int i = 0; i < n; i++) {
		int k = i, cost = n;
		while (mask & (1 << k)) k = (k + 1) % n, cost--;
		ans += cost + find (mask + (1 << k));
	}
	//cerr << mask << ' ' << ans << '/' << n << endl;
	return res = ans / n;
}

double solve() {
	string s; cin >> s; n = s.size();
	for (int i = 0; i < (1 << n); i++) d[i] = -1;
	int mask = 0;
	for (int i = 0; i < s.size(); i++) if (s[i] == 'X') mask += (1 << i);
	return find (mask);
}

main() {
	ios::sync_with_stdio (false);
	
	cout << fixed << setprecision (10);
	int tests; cin >> tests;
	for (int o = 1; o <= tests; o++) {
		cerr << "test " << o << endl;
		double ans = solve();
		cout << "Case #" << o << ": " << ans << endl;
	}

	return 0;
}
