#include "bits/stdc++.h"
 
using namespace std;
 
#define debug(x) cerr << "DEBUG: " << #x << " = " << x << endl
#define forn(i, n) for(int i = 0; i < (n); ++i)
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
#define mp make_pair
#define pb push_back
#define PATH "C:\\Users\\ValenKof\\Desktop\\"
 
template<typename T> inline void mn(T& x, const T& y) { if (y < x) x = y; }
template<typename T> inline void mx(T& x, const T& y) { if (x < y) x = y; }
template<typename T> inline int sz(const T& x) { return x.size(); }
 
typedef unsigned char uchar;
 
// SOLUTIONS BEGINS HERE

typedef long long ll;

ll readNum()
{
	double x;
	cin >> x;
	return (int) (x * 1e4 + 0.5);
}

long double temp(const vector<pair<ll, ll>>& a, long double need)
{
	long double v = 0.0;
	long double t = 0.0;
	for (auto p : a) {
		long double currentV = min((long double) p.second, need - v);
		long double currentT = p.first;
		
		t = (v * t + currentV * currentT) / (v + currentV);
		v = (v + currentV);
		
	}
	return t;
}

void solve() {
	int n;
	cin >> n;
	ll v = readNum();
	ll x = readNum();
	
	vector<ll> r(n), c(n);
	forn (i, n) {
		r[i] = readNum();
		c[i] = readNum();
	}
	
	
	ll minC = *min_element(all(c));
	ll maxC = *max_element(all(c));
	
	if (minC <= x && x <= maxC) {

		vector<pair<ll, ll>> sorted(n);
		forn (i, n) {
			sorted[i] = {c[i], r[i]};
		}
		sort(all(sorted));

		long long maxVolume = accumulate(all(r), 0L);
				
		long double l = 0;
		long double r = maxVolume;
		
		forn (iter, 200) {
			long double m = (l + r) / 2;
			long double minTemp = temp(sorted, m);
			reverse(all(sorted));
			long double maxTemp = temp(sorted, m);
			reverse(all(sorted));
			if (minTemp <= x && x <= maxTemp) {
				l = m;
			} else {
				r = m;
			}			
		}
		
		cout << fixed << setprecision(9) << (double) (v / l);
		return;
	}
	cout << "IMPOSSIBLE";
}
 
int main() {
	freopen(PATH"B-small-attempt0.in", "r", stdin);
	freopen(PATH"out.txt", "w", stdout);
	int nTests;
	cin >> nTests;
	forn (i, nTests) {
		cout << "Case #" << (i + 1) << ": ";
		solve();
		cout << endl;
	}	
	return 0;
}