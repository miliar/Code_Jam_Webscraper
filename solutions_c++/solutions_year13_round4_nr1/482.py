#include <cstdio>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <vector>

using namespace std;

#define debug(x) cerr << fixed << setprecision(3) << "DEBUG: " << #x << " = " << x << endl
#define sz(x) ((int)(x.size()))
#define pb push_back
#define mp make_pair
#define all(x) x.begin(), x.end()
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define DESKTOP "C:\\Users\\Malkav\\Desktop\\"
#define DOWNLOADS "C:\\Users\\Malkav\\Downloads\\"
#define out(...) printf(__VA_ARGS__), fprintf(stderr, __VA_ARGS__)

#define TASK "A-small-attempt0"

typedef long long ll;

struct Arc {
	ll from;
	ll to;
	ll count;
	Arc(ll from = 0, ll to = 0, ll count = 0) : from(from), to(to), count(count) { }
};

int n, m;

long long cost(Arc arc) {
	return arc.count * (arc.to - arc.from) * (n + (n - arc.to + arc.from - 1)) / 2;
}


long long solve() {
	vector<Arc> arcs(m);
	ll init = 0;
	for (int i = 0; i < m; ++i) {
		cin >> arcs[i].from >> arcs[i].to >> arcs[i].count;
		init += cost(arcs[i]);
	}
	
	while (true) {
		bool changed = false;
		
		for (int i = 0; i < sz(arcs); ++i) {
			if (arcs[i].count == 0) {
				swap(arcs[i], arcs.back());
				arcs.pop_back();
				--i;
			}
		}
		
		for (int i = 0; i < sz(arcs); ++i) {
			if (arcs[i].count == 0) {
				continue;
			}
			for (int j = 0; j < sz(arcs); ++j) {
				if (arcs[i].from < arcs[j].from && arcs[i].to < arcs[j].to && arcs[i].to >= arcs[j].from) {
					ll b = min(arcs[i].count, arcs[j].count);
					ll s = min(arcs[i].count, arcs[j].count);
					if (b == 0) {
						continue;
					}
					ll l = arcs[i].count - b;
					ll r = arcs[j].count - b;
					arcs[i].count = l;
					arcs[j].count = r;
					arcs.push_back(Arc(arcs[i].from, arcs[j].to, b));
					arcs.push_back(Arc(arcs[j].from, arcs[i].to, s));					
				}
			}
		}
		if (!changed) {
			break;
		}
	}
	for (int i = 0; i < sz(arcs); ++i) {
		init -= cost(arcs[i]);
	}
	
	return init;
}


int main() {
	freopen(DOWNLOADS TASK ".in", "r", stdin);
	freopen(DESKTOP TASK ".out", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cin >> n >> m;
		long long ans = solve();
		cout << "Case #" << (i + 1) << ": " << ans << endl;
	}
	return 0;
}