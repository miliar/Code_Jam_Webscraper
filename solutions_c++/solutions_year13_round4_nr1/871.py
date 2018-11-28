#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;

#define mp make_pair
#define pb push_back
#define rep(i, n) for(int (i) = 0; (i) < (n); ++(i))
#define repr(i, l, r) for(int (i) = (l); (i) < (r); ++(i))
#define clr(t, v) memset((t), (v), sizeof(t))
#define all(x) (x).begin(), (x).end()
#define sz(x) ((int)(x).size())
#define fi first
#define se second

#define DEBUG

int T, M;
ll N;
const ll MOD = 1000002013;

inline int calc_cost(ll dist) { return dist * (2*N + 1 - dist) / 2;}

vector<pair<pii, ll> > Mast;

int main() {
#ifdef DEBUG
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	scanf("%d", &T);

	rep(asdf, T) {
		scanf("%d%lld", &N, &M);
		Mast.clear();
		Mast.reserve(2*M);
		ll proper = 0;

		rep(i, M) {
			int a, b; ll c;
			scanf("%d%d%lld", &a, &b, &c);
			proper += calc_cost(b-a) * c;
			Mast.pb(mp(mp(a, 0), c));
			Mast.pb(mp(mp(b, 1), c));
		}
		sort(Mast.begin(), Mast.end());

		rep(it, Mast.size()-1) {
			//printf("%d", Mast[i].fi.fi);
			if (Mast[it].fi == Mast[it+1].fi) {
				Mast[it].se += Mast[it+1].se;
				Mast.erase(Mast.begin()+it+1);
				it--;
			}
		}
		set<pair<int, ll> > S;
		ll nval = 0;
		rep(i, Mast.size()) {
			if (Mast[i].fi.se == 0) {
				S.insert(mp(Mast[i].fi.fi, Mast[i].se));
			} else {
				ll a = Mast[i].se;
				while(a) {
					set<pair<int, ll> >::reverse_iterator it = S.rbegin();
					ll val = min(it->se, a);
					a -= val;
					nval += calc_cost(Mast[i].fi.fi - it->fi) * val;
					ll left = it->se - val;
					int beg = it->fi;
					S.erase(*it);
					if (left > 0) {
						S.insert(mp(beg, left));
					}
				}
			}
		}
		printf("Case #%d: %lld\n", asdf+1, (proper - nval) % MOD);
	}
	return 0;
}