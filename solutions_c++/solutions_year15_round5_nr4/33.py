// .... .... .....!
// ...... ......!
// .... ....... ..... ..!

#include<bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0, _n = (int)(n); i < _n; i++)
#define fer(i, x, n) for (int i = (int)(x), _n = (int)(n); i < _n; i++)
#define rof(i, n, x) for (int i = (int)(n), _x = (int)(x); i-- > _x; )
#define sz(x) (int((x).size()))
#define pb push_back
#define all(X) (X).begin(),(X).end()
#define X first
#define Y second

template<class P, class Q> inline void smin(P &a, Q b) { if (b < a) a = b; }
template<class P, class Q> inline void smax(P &a, Q b) { if (a < b) a = b; }

typedef long long ll;
typedef pair<int, int> pii;

////////////////////////////////////////////////////////////////////////////////

const int maxp = 10000 + 10;

int n;
int p;
ll e[maxp];
ll f[66][maxp];
int zero;

bool doit(ll val, int k) {
	if(val == 0) {
		rep(i, p) {
			if(f[k][i] % 2 == 1) return false;
			f[k+1][i] = f[k][i] / 2;
		}
		return true;
	}
	int t = 0;
	ll *v = f[k+1];
	rep(i, p) v[i] = f[k][i];

	if(val > 0) {
		rep(i, p) if(v[i]) {
			while(t < p && e[t] < e[i] + val) t++;
			if(t == p || e[t] != e[i] + val || v[i] > v[t]) return false;
			v[t] -= v[i];
		}
	} else {
		val = -val;
		rep(i, p) if(v[i]) {
			while(t < p && e[t] < e[i] + val) t++;
			if(t == p || e[t] != e[i] + val || v[i] > v[t]) return false;
			v[t] -= v[i];
		}
		rep(i, p) v[i] = f[k][i] - v[i];
	}
	if(accumulate(v, v+p, 0LL) != (1LL << (n-k-1))) return false;
	if(v[zero] == 0) return false;
	return true;
}

ll ans[66];

void go(int k) {
	if(k == n) throw 0;

	int pos = 0;
	while(f[k][pos] == 0) pos++;

	rof(i, p, pos+1) {
		ll cur = e[pos] - e[i];
		ans[k] = cur;
		if(doit(cur, k)) go(k+1);
	}
	ans[k] = 0;
	if(doit(0, k)) go(k+1);
	fer(i, pos+1, p) {
		ll cur = e[i] - e[pos];
		ans[k] = cur;
		if(doit(cur, k)) go(k+1);
	}
}

void solve() {
	ll tot = 0;

	cin >> p;
	rep(i, p) cin >> e[i];
	rep(i, p) cin >> f[0][i], tot += f[0][i];

	n = 0;
	while(tot > 1) tot /= 2, n++;

	zero = 0;
	while(e[zero] < 0) zero++;

	try {
		go(0);
	} catch(...) {
		rep(i, n) cout << ' ' << ans[i];
		cout << endl;
	}
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);

	int ttt; cin >> ttt;
	fer(ttc, 1, ttt+1) {
		cout << "Case #" << ttc << ":";
		solve();
	}

	return 0;
}

