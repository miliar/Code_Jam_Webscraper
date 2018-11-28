#include <bits/stdc++.h>
using namespace std;
#define FOR(i,a,b) for(int i=(a); i<(b); ++i)
//#define REP(i,n) FOR(i,1,(n)+1)
typedef vector<int> vi;
#define pb push_back
#define sz size()
typedef pair<int,int> pii;
#define mp make_pair
#define st first
#define nd second
typedef long long ll;
#define INF 1000000001
//#define VAR(n,v) typeof(v) n=(v)
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
	GET(t);
	FOR(ti,1,t+1) {
		GET(x);
		GET(r);
		GET(c);
		int a = r*c;
		static const int GABRIEL = 0;
		static const int RICHARD = 1;
		int wins;
		switch(x) {
		    case 1:
			wins = GABRIEL;
			break;
		    case 2:
			wins = (a % 2 == 0) ? GABRIEL : RICHARD;
			break;
		    case 3:
			if((r<3 && c<3) || r==1 || c==1 || a%3) wins = RICHARD;
			else wins = GABRIEL;
			break;
		    case 4:
			if((r<4 && c<4) || min(r,c) < 3) wins = RICHARD;
			else wins = GABRIEL;
			break;
		}
		//dprintf("%d %d %d\n", x, r, c);
		printf("Case #%d: %s\n", ti,
		    (GABRIEL == wins) ? "GABRIEL" : "RICHARD");        
	}
	return 0;
}
