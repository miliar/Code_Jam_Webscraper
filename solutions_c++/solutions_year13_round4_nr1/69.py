#include <algorithm>
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

const int maxN = 1000 + 100;
const int mod = 1000002013;

int n, m;
int o[maxN], e[maxN], p[maxN];

int solve() {
	cin >> n >> m;
	int normal = 0, cheat = 0;
	vector <pair <pie, int> > v;
	for (int i = 0; i < m; i++) {
		cin >> o[i] >> e[i] >> p[i]; 
		int l = e[i] - o[i];
		normal = (normal + p[i] * ((l * n - l * (l - 1) / 2) % mod)) % mod;
		v.push_back (mp (pie (o[i], 0), p[i]));
		v.push_back (mp (pie (e[i], 1), p[i]));
	}
	sort (v.begin(), v.end());
	vector <pie> stack;
	for (int i = 0; i < v.size(); i++) {
		if (v[i].ff.ss) 
			while (stack.size() && v[i].ss) {
				pie x = stack.back();
				int l = v[i].ff.ff - x.ff;
	//			cerr << "stack " << v[i].ff.ff << ' ' << x.ff << ' ' << x.ss << endl;
				if (x.ss > v[i].ss) {
	//				cerr << l << ' ' << v[i].ss << endl;
					cheat = (cheat + v[i].ss * ((l * n - l * (l - 1) / 2) % mod)) % mod;
					stack[stack.size() - 1].ss -= v[i].ss;
					v[i].ss = 0;
					break;
				}
				else {
	//				cerr << l << ' ' << x.ss << endl;
					cheat = (cheat + x.ss * ((l * n - l * (l - 1) / 2) % mod)) % mod;
					v[i].ss -= x.ss;
					stack.pop_back();
				}
			}
		else {
	//		cerr << v[i].ff.ff << ' ' << v[i].ss << ' ' << "add " << endl;
			stack.push_back (pie (v[i].ff.ff, v[i].ss));
		}
	}
	//cerr << normal << ' ' << cheat << endl;

	return ((normal - cheat) % mod + mod) % mod;
}

main() {
	ios::sync_with_stdio (false);
	
	int tests; cin >> tests;
	for (int o = 1; o <= tests; o++) {
		int ans = solve();
		cout << "Case #" << o << ": " << ans << endl;
	}

	return 0;
}
