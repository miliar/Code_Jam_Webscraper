#ifdef DEBUG
#define debug printf("OK\n")
#else
#define debug //
#endif

#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
using namespace std;

#define REP(i, n) for(int (i)=0; (i)<(n); (i)++)
typedef pair<int, int> ii;
typedef long long int ll;
typedef pair<int, ll> il;
#define x first
#define y second
#define MOD 1000002013

int T, N, M;

ll cost (int dist) {
	ll ans = 0;
	ans = ((ll)N)*dist - (((ll)dist)*(dist-1))/2;
	ans %= MOD;
	return ans;
}

vector<il> st, ed;

int bin(int i) {
	int lo=0, hi=M-1, mid, ans;
	while(true) {
		if (hi<lo) return ans;
		mid = (hi+lo)/2;
		if (i>=st[mid].x) {
			lo = mid+1;
			ans = mid;
		}
		else hi = mid-1;
	}
}


int main () {
	scanf("%d", &T);
	int tt1, tt2;
	ll tt3;
	REP(mm, T) {
		scanf("%d%d", &N, &M);
		ll act = 0;
		st.clear(); ed.clear();
		REP(i, M) {
			scanf("%d%d%lld", &tt1, &tt2, &tt3);
			st.push_back(il(tt1, tt3));
			ed.push_back(il(tt2, tt3));
			act += tt3*cost(tt2-tt1);
			act %= MOD;
		}
		sort(st.begin(), st.end());
		sort(ed.begin(), ed.end());
		
		ll ans = 0, tmp;
		
		REP(i, M) {
			ll peo = ed[i].y;
			int ind = bin(ed[i].x);
			while (peo>0) {
				tmp = min(st[ind].y, peo);
				peo -= tmp;
				st[ind].y -= tmp;
				ans += tmp * cost(ed[i].x-st[ind].x);
				ans %= MOD;
				ind--;
			}
		}
		printf("Case #%d: ", mm+1);
		if (act>=ans) printf("%lld\n", act-ans);
		else printf("%lld\n", act+MOD-ans);
	}
}
