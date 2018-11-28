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

const int maxn = 1000 + 100;

int n, k;
int sum[maxn];
int a[maxn];
pii p[maxn];
multiset<pii> ms;
multiset<pii> rs;

inline pii rev(pii tmp) {
	return pii(-tmp.Y, -tmp.X);
}

bool can(int d) {
	rep(i, k) if(p[i].Y - p[i].X > d) return false;
	int lo = -1e9, hi = 1e9;
	while(hi - lo > 1) {
		int md = (lo+hi) / 2;
		ll lf = 0, rg = 0;
		rep(i, k) lf += (ll)md - p[i].X, rg += (ll)md + d - p[i].Y;
		if(rg < 0)
			lo = md;
		else if(lf > 0)
			hi = md;
		else
			return true;
	}
	return false;
}

int solve() {
	cin >> n >> k;
	rep(i, n-k+1) cin >> sum[i];
	if(sum[0] < 0)
		rep(i, n-k+1) sum[i] *= -1;

	rep(i, k) p[i].X = 0, p[i].Y = 0;

	rep(i, k) a[i] = 0;
	fer(i, k, n) {
		a[i] = sum[i-k+1] - sum[i-k] + a[i-k];
		smin(p[i % k].X, a[i]);
		smax(p[i % k].Y, a[i]);
	}

	if(k == 1) return p[0].Y - p[0].X;

	p[k-1].X += sum[0], p[k-1].Y += sum[0];

	int zz = 0;
	for(pii t: ms) p[zz++] = t;

	int lo = -1, hi = 1e9;
	while(hi - lo > 1) {
		int md = (lo + hi) / 2;
		if(can(md))
			hi = md;
		else
			lo = md;
	}
	
	int ans = hi;
	
	return ans;
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);

	int ttt; cin >> ttt;
	fer(ttc, 1, ttt+1) {
		cout << "Case #" << ttc << ": " << solve() << endl;
	}

	return 0;
}

