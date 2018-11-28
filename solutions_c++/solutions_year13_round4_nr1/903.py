#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
using namespace std;
#define VAR(n,v) typeof(v) n=(v)
#define REP(i,n) for(int i=1; i<=(n); ++i)
#define FOR(i,a,b) for(VAR(i,a); i!=(b); ++i)
#define FORE(it,t) FOR(it,t.begin(),t.end())
typedef vector<int> vi;
#define pb push_back
typedef pair<int,int> pii;
#define mp make_pair
#define st first
#define nd second
typedef long long ll;
#define INF 1000000001
#define sz size()
#define ALL(t) t.begin(),t.end()
#define SC(a) scanf("%d", &a)
#define GET(a) int a; SC(a)
#ifdef DEBUG
	#define dprintf(...) do{printf("\033[31m"); printf(__VA_ARGS__); printf("\033[0m");}while(0)
	template <class It> void dptab(It b, It e, const char* f="%d ")
		{for(It it=b; it!=e; ++it) dprintf(f, *it); dprintf("\n"); }
#else
	#define dprintf(...)
	template <class It> void dptab(It b, It e, const char* f="%d ") {}
#endif

#define P 1000002013

int n;

ll cost(ll l) {
	return (l*n + l - l*(l+1)/2) % P;
}

int test() {
	SC(n); GET(m);
	vector<pii> ev;
	ll due = 0;
	REP(i,m) {
		GET(o); GET(e); GET(p);
		due += (p * cost(e-o)) % P;
		ev.pb(mp(o,-p));
		ev.pb(mp(e,p));
	}
	sort(ALL(ev));
	vector<pii> tck;
	ll real = 0;
	FORE(iev, ev) {
		int x = iev->st, p = -iev->nd;
		dprintf("event (%d, %d)\n", x, p);
		if(p > 0) tck.pb(mp(x, p));
		else {
			p = -p;
			while(p) {
				int pi = min(p, tck.back().nd);
				p -= pi; tck.back().nd -= pi;
				real += (pi * cost(x - tck.back().st)) % P;
				dprintf("\t%lld\n", real);
				if(tck.back().nd == 0)
					tck.pop_back();
			}
		}
	}
	return (due - real) % P;
}

int main() {
	GET(T);
	REP(t,T)
		printf("Case #%d: %d\n", t, test());
}

