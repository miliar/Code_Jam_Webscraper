#include <cstdio>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <vector>
#include <algorithm>

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

#define TASK "B-large"

typedef long long ll;

ll solve_min(int n, ll p) {
	ll l = 0;
	ll r = 1LL << n;
	ll total = 1LL << n;
	while (r - l > 1) {
		ll m = (l + r) / 2;
		
		ll x = m;
		ll y = total - m - 1;
		
		int win = 0;
		while (y > 0) {
			ll yy = (y - 1) / 2;
			ll xx = (x + 1) / 2;
			y = yy;
			x = xx;
			win++;			
		}
		ll mask = 0;
		for (int i = 0; i < n - win; ++i) {
			mask |= (1LL << i);
		}
		bool can_win = mask < p;
		if (can_win) {
			l = m;
		} else {
			r = m;
		}
	}
	return l;
}

ll solve_max(int n, ll p) {
	ll l = 0;
	ll r = 1LL << n;
	ll total = 1LL << n;
	while (r - l > 1) {
		ll m = (l + r) / 2;
		
		ll x = m;
		ll y = total - m - 1;
		
		int lose = 0;
		while (x > 0) {
			ll yy = (y + 1) / 2;
			ll xx = (x - 1) / 2;
			y = yy;
			x = xx;
			lose++;			
		}
		ll mask = 0;
		for (int i = 0; i < lose; ++i) {
			mask |= (1LL << (n - 1 - i));
		}
		bool can_lose = mask >= p;
		if (can_lose) {
			r = m;
		} else {
			l = m;
		}
	}
	return l;
}


pair<ll, ll> solve(int n, ll p) {
	ll f = solve_max(n, p);
	ll s = solve_min(n, p);
	
	return mp(f, s);	
}

int main() {
	freopen(DOWNLOADS TASK ".in", "r", stdin);
	freopen(DESKTOP TASK ".out", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		int n;
		ll p;
		cin >> n >> p;
		pair<ll, ll> ans = solve(n, p);
		cout << "Case #" << (i + 1) << ": " << ans.first << " " << ans.second << endl; 
	}
	return 0;
}