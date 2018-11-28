#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <bitset>
#include <queue>
#include <stack>
#include <sstream>
#include <cstring>
#include <numeric>
#include <ctime>

#define re return
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define sz(x) ((int) (x).size())
#define rep(i, n) for (int i = 0; i < (n); i++)
#define rrep(i, n) for (int i = (n) - 1; i >= 0; i--)
#define y0 y32479
#define y1 y95874
#define fill(x, y) memset(x, y, sizeof(x))
#define sqr(x) ((x) * (x))
#define sqrt(x) sqrt(abs(x))
#define unq(x) (x.resize(unique(all(x)) - x.begin()))
#define spc(i,n) " \n"[i == n - 1]

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;
typedef double D;
typedef long double LD;
typedef long long ll;
typedef pair<ll, ll> pll;
typedef vector<ll> vll;

template<class T> T abs(T x) { return x > 0 ? x : -x;}

ll m;
ll n;

ll get1(ll x, ll n) {
	if (x == 0)
		re 0;
	re get1((x - 1) / 2, n - 1) + (1ll << (n - 1));
}

ll get2(ll x, ll n) {
	if (x == (1ll << n) - 1)
		re (1ll << n) - 1;
	re get2((x + 1) / 2, n - 1);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tc;
	cin >> tc;
	rep(tt, tc) {
		cout << "Case #" << tt + 1 << ": ";
		cin >> n >> m;

		ll l = 0, r = (1ll << n) - 1;
		ll sc = r;

		while (l <= r) {
			ll c = (l + r) / 2;
			if (get1(c, n) < m) {
				sc = c;
				l = c + 1;
			}
			else
				r = c - 1;
		}
		cout << sc << ' ';

		/*rrep(i, 1 << n) {
			if (get1(i, n) < m) {
				cout << i << ' ';
				break;
			}
		}*/

		l = 0, r = (1ll << n) - 1;
		while (l <= r) {
			ll c = (l + r) / 2;
			if (get2(c, n) < m) {
				sc = c;
				l = c + 1;
			}
			else
				r = c - 1;
		}
		cout << sc << endl;

/*		rrep(i, 1 << n) {
			if (get2(i, n) < m) {
				cout << i << endl;
				break;
			}
		}*/
	}



	re 0;
}

