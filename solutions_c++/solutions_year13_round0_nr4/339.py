#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <bitset>
#include <queue>
#include <sstream>
using namespace std;
#define clr(a,x) memset(a, x, sizeof(a))
#define all(v) (v).begin(), (v).end()
#define iter(v) __typeof((v).begin())
#define foreach(it, v) for (iter(v) it = (v).begin(); it != (v).end(); it++)
#define pb push_back
#define mp make_pair
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for (int i = (int)(a); i <= (b); i++)
typedef long long ll;
typedef pair <int,int> PII;
ll sqr(ll x) {return x * x;}
template <class T> void checkmax(T &t, T x){if (x > t) t = x;}
template <class T> void checkmin(T &t, T x){if (x < t) t = x;}
template <class T> void _checkmax(T &t, T x){if (t == -1 || x > t) t = x;}
template <class T> void _checkmin(T &t, T x){if (t == -1 || x < t) t = x;}
ll power_mod(ll a, int b, int p) {
	ll ret = 1;
	for (; b; b >>= 1) {
		if (b & 1) ret = ret * a % p;
		a = a * a % p;
	}
	return ret;
}
const int N = 20;
int m, n;
int f[1 << 20];
vector <int> my[1 << 20];
int T[N];
vector <int> keys[N];

int main() {
	//freopen("in", "r", stdin);
	int Tc;
	cin >> Tc;
	rep (_, Tc)	{
		printf("Case #%d: ", _ + 1);
		vector <int> v;
		cin >> m >> n;
		rep (i, m) {
			int x;
			scanf("%d", &x);
			v.pb(x);
		}
		rep (i, n) {
			cin >> T[i] >> m;
			keys[i].clear();
			rep (j, m) {
				int x;
				scanf("%d", &x);
				keys[i].pb(x);
			}
		}
		clr(f, 0xff);
		f[0] = 0;
		rep (mask, 1 << n) my[mask].clear();
		rep (mask, 1 << n) {
			if (f[mask] == -1) continue;
			vector <int> u = v;
			rep (i, n)
				if (mask & 1 << i)
					u.insert(u.end(), keys[i].begin(), keys[i].end());
			sort(u.begin(), u.end());
			rep (i, n)
				if (mask & 1 << i) {
					u.erase(lower_bound(u.begin(), u.end(), T[i]));
				}
			rep (i, n)
				if (!(mask & 1 << i) && binary_search(u.begin(), u.end(), T[i])) {
					int &tmp = f[mask | 1 << i];
					vector <int> res = my[mask];
					res.pb(i);
					if (tmp == -1) {
						tmp = i;
						my[mask | 1 << i] = res;
					} else if (res < my[mask | 1 << i]) {
						my[mask | 1 << i] = res;
					}
				}
		}
		if (f[(1 << n) - 1] == -1) {
			puts("IMPOSSIBLE");
		} else {
			vector <int> ans;
			int mask = (1 << n) - 1;
			rep (i, n)
				cout << my[mask][i] + 1 << ((i + 1 == n) ? '\n' : ' ');
		}
	}
	return 0;
}
