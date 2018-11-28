#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <string>
using namespace std;
#define pii pair<int, int>
#define pdd pair<double, double>
#define mp make_pair
#define x first
#define y second
#define L(s) ((int)(s).size())
#define pb push_back
#define VI vector<int>
#define ll long long
#define all(s) (s).begin(), (s).end()
int t, n;
ll x[77], b, y[77];
inline ll get_cost(int put, int skip, ll lim) {
	for(int i = 0; i < n; ++i) y[i] = x[i];
	ll cost = 0;
	for(int i = 0; i < put; ++i) {
		cost += lim - x[i];
		y[i] = lim;
	}
	int alr = 0;
	for(int i = put; i < n; ++i) {
		if (x[i] <= lim) {
			cost += (lim + 1 - x[i]);
			++alr;
			y[i] = lim + 1;
			if (alr == skip) break;
		}
	}
	return cost;
}
inline double get_gain(int put, int skip, ll lim) {
	ll minval = *min_element(y, y + 37);
	ll mincnt = 0;
	for(int i = 0; i < n; ++i) if (y[i] == minval) mincnt++;
	double gain = 0;
	for(int i = 0; i < put; ++i) {
		if (y[i] == minval)
			gain += 36. * (lim - x[i]) / mincnt;
	}
	return gain;
}
inline void go(int put, int skip, ll lim, double &ans) {
	ll cost = get_cost(put, skip, lim);
	if (cost > b) return;
	double gain = get_gain(put, skip, lim);
	ans = max(ans, gain - cost);
}
int main() {
	freopen("A-large (1).in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	for(int tc = 1; tc <= t; ++tc) {
		cerr << tc << endl;
		cin >> b >> n;
		for(int i = 0; i <= 36; ++i) {
			x[i] = 0;
		}
		for(int i = 0; i < n; ++i) {
			cin >> x[i];
		}
		n = 37;
		sort(x, x + n);
		double ans = 0.;
		for(int put = 1; put <= n; ++put) {
			for(int skip = 0; skip + put <= n; ++skip) {
				ll low = x[put - 1];
				if (get_cost(put, skip, low) > b) continue;
				ll high = (ll)1e15;
				while(high - low > 1) {
					ll mid = (high + low) / 2;
					if (get_cost(put, skip, mid) > b) high = mid; else low = mid;
				}
				go(put, skip, x[put - 1], ans);
				for(ll lim = max(low - 10, x[put - 1]); lim <= low; ++lim) {
					go(put, skip, lim, ans);
				}
			}
		}
		printf("Case #%d: %0.9lf\n", tc, ans);
	}
} 