#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <deque>
#include <bitset>

#define sqr(x) ((x) * (x))
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define y0 ywuerosdfhgjkls
#define y1 hdsfjkhgjlsdfhgsdf
#define j1 j924
#define j0 j2834
#define sqrt(x) (sqrt(abs(x)))
#define re return
#define sz(x) ((int)(x).size())
#define all(x) (x).begin(), (x).end()
#define rep(i, n) for (int i = 0; i < (n); i++)
#define rrep(i, n) for (int i = ((n) - 1); i >= 0; i--)
#define fill(a, x) memset(a, x, sizeof(a))

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair <int, int> ii;
typedef vector <int> vi;
typedef vector <ii> vii;
typedef vector <vi> vvi;
typedef double D;
typedef vector <string> vs;

template <class T> inline T abs(T a) {
	return a > 0 ? a : -a;
}

int n;
int m;

const ll mod = 1000002013;

int main() {
	int T;
	cin >> T;
	rep(I, T) {
		ll n;
		int m;
		pair <ll, ll> s[10000];
		ll p[10000];
		cin >> n >> m;
		ll sum = 0;
		set <int> stat;
		rep(i, m) {
			cin >> s[i].fi >> s[i].se >> p[i];
			//cerr << s[i].fi << ' ' << s[i].se << ' ' << p[i] << endl;
			stat.insert(s[i].fi);
			stat.insert(s[i].se);
			ll cost = (n * (s[i].se - s[i].fi) - (s[i].se - s[i].fi) * (s[i].se - s[i].fi - 1) / 2) % mod;
			sum += p[i] * cost % mod;
			sum %= mod;
		}
		//cerr << sum << endl;
		map <int, int> num;
		int cnt = 0;
		int S[20000];
		for (set <int> :: iterator it = stat.begin(); it != stat.end(); it++) {
			num[*it] = cnt++;
			S[cnt - 1] = *it;
		}
		ll ans = 0;
		pair <ll, ll> ev[20000];
		cnt = 0;
		for (int i = 0; i < m; i++) {
			//cerr << num[s[i].fi] << ' ' << num[s[i].se] << ' ' << p[i] << endl;
			ev[cnt].fi = num[s[i].fi];
			ev[cnt++].se = -p[i];
			ev[cnt].fi = num[s[i].se];
			ev[cnt++].se = p[i];
			//cerr << num[s[i].fi] << ' ' << num[s[i].se] << endl;
		}
		//cerr << sum << endl;
		sort(ev, ev + 2 * m);

		ll ssum = 0;
		ll k[20000];
		fill(k, 0);
		for (int i = 0; i < 2 * m; i++) {
			if (ev[i].se > 0) {
				ev[i].se = ev[i].se;
				/*rep(j, 2 * m) {
					cerr << k[j] << ' ';
				}
				cerr << endl;*/
				rrep(j, 2 * m) {
					//cerr << i << ' ' << j << ' ' << ev[i].se << ' ' << k[j] << endl;
					ll q = min(ev[i].se, k[j]);
					ll cost = ((S[ev[i].fi] - S[j]) * n - (S[ev[i].fi] - S[j]) * (S[ev[i].fi] - S[j] - 1) / 2) % mod;
					ssum += q * cost % mod;
					ssum %= mod;
					ev[i].se -= q;
					k[j] -= q;
				}
			} else {
				//cerr << i << endl;
				k[ev[i].fi] -= ev[i].se;
			}
		}
		//cerr << ssum << endl;
		cout << "Case #" << I + 1 << ": " << (sum - ssum + mod) % mod  << endl;
	}
	return 0;
}
