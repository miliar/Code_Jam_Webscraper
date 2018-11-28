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
#define FOR(i,a,b) for(int i=(a); i<(b); ++i)
#define REP(i,n) FOR(i,1,(n)+1)
typedef vector<int> vi;
#define pb push_back
typedef pair<int,int> pii;
#define mp make_pair
#define st first
#define nd second
typedef long long ll;
#define INF 1000000001
#define sz size()
#define VAR(n,v) typeof(v) n=(v)
#define ALL(t) t.begin(),t.end()
#define SC(a) scanf("%d", &a)
#define GET(a) int a; SC(a)
#define ISDEBUG 1
#define dprintf(...) if(ISDEBUG) \
{printf("\033[31m"); printf(__VA_ARGS__); printf("\033[0m");}
template <class It> void dptab(It b, It e, const char* f="%.3lf ") {
	if(ISDEBUG) {
		for(It it=b; it!=e; ++it) dprintf(f, *it); dprintf("\n");
}}

int main() {
	GET(t);
	FOR(ti, 0, t) {
		GET(n);
		vector<double> ken, naomi;
		FOR(i,0,n) {
			double x;
			scanf("%lf", &x);
			naomi.pb(x);
		}
		FOR(i,0,n) {
			double x;
			scanf("%lf", &x);
			ken.pb(x);
		}
		
		sort(ALL(ken));
		sort(ALL(naomi));
		
		
		
		int score2 = 0, score = 0;
		reverse(ALL(ken));
		reverse(ALL(naomi));

		//dptab(ALL(ken));
		//dptab(ALL(naomi));

		int w=0;
		
		FOR(i,0,n) {
			if(ken[i]>naomi[w]) {

			} else {
				++w;
				score++;
			}
		}
		
		reverse(ALL(ken));
		w = n-1;
		FOR(i, 0, n) {
			if(ken[w] > naomi[i]) {
				--w;
			} else {
				score2++;
			}
		}
		
		printf("Case #%d: %d %d\n", ti+1, score, score2);
	}
	return 0;
}
