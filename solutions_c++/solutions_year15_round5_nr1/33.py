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

const int maxn = 1000000 + 100;

int n, d;
int s[maxn], m[maxn];
int par[maxn];
vector<int> child[maxn];
pii p[maxn];
multiset<int> ms;

void dfs(int u, int mn = 1e9, int mx = -1e9) {
	smin(mn, s[u]);
	smax(mx, s[u]);
	p[u] = {mn, mx};
	for(int v: child[u]) dfs(v, mn, mx);
}

int solve() {
	cin >> n >> d;
	int as, cs, rs, am, cm, rm;
	cin >> s[0] >> as >> cs >> rs;
	cin >> m[0] >> am >> cm >> rm;

	fer(i, 0, n-1) {
		s[i+1] = (s[i] * (ll)as + cs) % rs;
		m[i+1] = (m[i] * (ll)am + cm) % rm;
	}

	fer(i, 1, n) {
		par[i] = m[i] % i;
		child[par[i]].pb(i);
	}

	dfs(0);

	sort(p, p+n, [](pii a, pii b) { return a.Y < b.Y; } );

	int ans = 1;
	rep(i, n) {
		ms.insert(p[i].X);
		while(!ms.empty() && p[i].Y - *ms.begin() > d)
			ms.erase(*ms.begin());
		smax(ans, sz(ms));
	}

	rep(i, n) child[i].clear();
	ms.clear();
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

