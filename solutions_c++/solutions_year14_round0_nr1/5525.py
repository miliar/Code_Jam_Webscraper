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
template <class It> void dptab(It b, It e, const char* f="%d ") {
	if(ISDEBUG) {
		for(It it=b; it!=e; ++it) dprintf(f, *it); dprintf("\n");
}}

int main() {
	GET(z);
	FOR(f,0,z) {
		set<int>s, s2;
		
		GET(a);
		--a;
		FOR(i, 0, 4)
			FOR(j, 0, 4) {
				GET(x);
				if(i==a) s.insert(x);
		}
		SC(a);
		--a;
		FOR(i, 0, 4)
			FOR(j, 0, 4) {
				GET(x);
				if(i==a && s.count(x)) s2.insert(x);
		}
		
		printf("Case #%d: ",f+1);
		switch(s2.sz) {
			case 0: printf("Volunteer cheated!\n"); break;
			case 1: printf("%d\n", *s2.begin()); break;
			default: printf("Bad magician!\n"); break;
		}
	}
	return 0;
}





