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
#define ISDEBUG 1
#define dprintf(...) if(ISDEBUG) \
	{printf("\033[31m"); printf(__VA_ARGS__); printf("\033[0m");}
template <class It> void dptab(It b, It e, const char* f="%d ")
	{if(ISDEBUG) {for(It it=b; it!=e; ++it) dprintf(f, *it); dprintf("\n"); }}

int main() {
	GET(t);
	REP(test,t) {
		GET(n); GET(m);
		vector<vi> t(n+1);
		vi cols(n+1,-INF), rows(m+1, -INF);
		REP(i,n) {
			t[i].resize(m+1);
			REP(j,m) {
				SC(t[i][j]);
				cols[i] = max(cols[i], t[i][j]);
				rows[j] = max(rows[j], t[i][j]);
			}
		}
		
		REP(i,n) REP(j,m)
			if(t[i][j] != cols[i] && t[i][j] != rows[j])
				goto nack;

		printf("Case #%d: YES\n", test);
		continue;
		nack:
			printf("Case #%d: NO\n", test);

	}
	return 0;	
}

