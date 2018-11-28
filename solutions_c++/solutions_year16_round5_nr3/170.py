#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef pair<ll,ll> pll;
typedef vector<bool> vb;
const ll oo = 0x3f3f3f3f3f3f3f3f;
const double eps = 1e-9;
#define sz(c) ll((c).size())
#define all(c) begin(c), end(c)
#define FOR(i,a,b) for (ll i = (a); i < (b); i++)
#define FORD(i,a,b) for (ll i = (b)-1; i >= (a); i--)
#define mp make_pair
#define mt make_tuple
#define pb push_back
#define eb emplace_back
#define xx first
#define yy second
#define has(c,i) ((c).find(i) != end(c))
#define DBGDO(X) ({ if(1) cerr << "DBGDO: " << (#X) << " = " << (X) << endl; })

vl p;

ll Find(ll x) {
	if (p[x] == x) return x;
	return p[x] = Find(p[x]);
}

bool Union(ll x, ll y) {
	x = Find(x), y = Find(y);
	if (x == y) return false;
	if (rand() & 1) swap(x,y);
	p[x] = y;
	return true;
}

int main() {
	ll TC; cin >> TC;
	FOR(tc,1,TC+1) {
		cout << "Case #" << tc << ": ";
		ll n, s; cin >> n >> s;
		vl x(n), y(n), z(n);
		FOR(i,0,n) {
			cin >> x[i] >> y[i] >> z[i] >> s >> s >> s;
		}
		p.resize(n);
		FOR(i,0,n) p[i] = i;
		
		vector<pair<ll,pll>> q;
		FOR(i,0,n) FOR(j,0,n) {
			ll dx = x[i] - x[j], dy = y[i] - y[j], dz = z[i] - z[j];
			q.pb(mp(dx*dx+dy*dy+dz*dz,pll(i,j)));
		}
		sort(all(q));
		for (auto e : q) {
			Union(e.yy.xx,e.yy.yy);
			if (Find(0) == Find(1)) {
				cout << fixed << setprecision(12) << sqrt(e.xx) << endl;
				break;
			}
		}

	}


}

