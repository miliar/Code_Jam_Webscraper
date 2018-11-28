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

int main() {
	ll TC; cin >> TC;
	FOR(tc,1,TC+1) {
		cout << "Case #" << tc << ": ";
		
		ll n, k; cin >> n >> k;
		vector<double> p(n);
		FOR(i,0,n) cin >> p[i];
		sort(all(p));
		
		double res = 0;
		FOR(i,0,k+1) {
			vector<double> pp;
			FOR(j,0,i) pp.pb(p[j]);
			FOR(j,n-k+i,n) pp.pb(p[j]);
			vector<double> q(k+1);
			q[0] = 1;
			FOR(i,0,k) {
				vector<double> nq(k+1);
				FOR(j,0,k) nq[j+1] += pp[i]*q[j], nq[j] += (1-pp[i])*q[j];
				q = nq;
			}
			res = max(res,q[k/2]);
		}
		cout << fixed << setprecision(12) << res << endl;
	}


}

