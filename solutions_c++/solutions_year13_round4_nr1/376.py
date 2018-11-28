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
const int mod = 1000002013;
int tc, n, m;
map<int, ll> start;
vector<pair<int, pii > > events;
inline int F(int len) {
	int big = ((ll)n * (n + 1) / 2) % mod;
	int small = ((ll)(n - len) * (n - len + 1) / 2) % mod;
	return (big - small + mod) % mod;
}
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> tc;
	for(int tn = 1; tn <= tc; ++tn) {
		cerr << tn << endl;
		cin >> n >> m;
		events.clear();
		int exp = 0;
		for(int i = 0; i < m; ++i) {
			int st, fn, cnt;
			cin >> st >> fn >> cnt;
			events.pb(mp(st, mp(0, cnt)));
			events.pb(mp(fn, mp(1, cnt)));
			int len = fn - st;
			exp = ((ll)exp + (ll)F(len) * cnt % mod) % mod;
		}
		int gained = 0;
		sort(all(events));
		start.clear();
		for(int i = 0; i < L(events); ) {
			int j = i;
			int pos = events[i].x;
			while(j < L(events) && events[j].x == pos && events[j].y.x == 0) {
				start[pos] += events[j].y.y;
				++j;
			}
			while(j < L(events) && events[j].x == pos && events[j].y.x == 1) {
				int cnt = events[j].y.y;
				while(cnt) {
					map<int, ll>::iterator it = start.end(); --it;
					if (cnt <= it->y) {
						gained = ((ll)gained + (ll)F(pos - it->x)  * cnt) % mod;
						start[it->x] -= cnt;
						cnt = 0;
					} else {
						gained = ((ll)gained + (ll)F(pos - it->x)  * it->y) % mod;
						cnt -= (int)it->y;
						start.erase(it);
					}
				}
				++j;
			}
			i = j;
		}
		int res = exp - gained; if (res < 0) res += mod;
		printf("Case #%d: %d\n", tn, res); 
	}
} 