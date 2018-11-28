#include <bits/stdc++.h>
#include <cstdint>

using namespace std;

#define mp make_pair
#define pb push_back
#define rep(i,n) for(int i = 0; i < (n); i++)
#define re return
#define fi first
#define se second
#define sz(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define sqrt(x) sqrt(abs(x))
#define y0 y3487465
#define y1 y8687969
#define j0 j5743892
#define j1 j542893
                         
typedef vector<int> vi;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef double D;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;
typedef vector<vi> vvi;

template<class T> T abs(T x) { re x > 0 ? x : -x; }
template<class T> T gcd(T a, T b) { re a ? gcd (b % a, a) : b; }
template<class T> T sqr(T a) { re a * a; }
template<class T> T sgn(T a) { re a > 0 ? 1 : (a < 0 ? -1 : 0); }

#define filename ""

int n;
int m;

int main () {
//	freopen (filename".in", "r", stdin);
//	freopen (filename".out", "w", stdout);	
	vector <pair <ll, vi>> ans;
	printf ("Case #1:\n");
	n = 32, m = 500;
	for (unsigned int i = 0; i < (1u << (n - 2)) && sz (ans) < m; i++) {
		ll kk = i * 2 + 1;
		kk |= (1ll << (n - 1));
		bool good = true;
		vi cur;
		for (int j = 2; j <= 10; j++) {
			bool ok = false;
			for (int p = 3; p < 1000; p++) {
				ll k = kk;
				ll res = 0;
				for (int i = 0; i < n; i++) {
					res = (res * j + (k >> (n - i - 1)) % 2) % p;
				}
				if (res == 0) { ok = true; cur.pb (p); break; }
			}
			if (!ok) { good = false; break; }
		}
		if (good) ans.pb (mp (kk, cur));
	}
	assert (sz (ans) == m);
	for (int i = 0; i < sz (ans); i++) {
		for (int j = 0; j < n; j++) printf ("%d", int((ans[i].fi >> (n - j - 1)) & 1));
		for (int j = 0; j < sz (ans[i].se); j++) {
			printf (" %d", ans[i].se[j]);
		}
		printf ("\n");
	}

	return 0;
}
