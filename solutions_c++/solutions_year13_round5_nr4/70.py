#include <sstream>
#include <iomanip>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <string>
#include <deque>
#include <complex>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; i--)
#define REP(i,a) for(int i=0,_a=(a); i<_a; i++)
#define ll long long
#define F first
#define S second
#define PB push_back
#define MP make_pair

#define DEBUG(x) cout << #x << " = "; cout << x << endl;
#define PR(a,n) cout << #a << " = "; FOR(_,1,n) cout << a[_] << ' '; cout << endl;
#define PR0(a,n) cout << #a << " = "; REP(_,n) cout << a[_] << ' '; cout << endl;
using namespace std;

//Buffer reading
int INP,AM,REACHEOF;
#define BUFSIZE (1<<12)
char BUF[BUFSIZE+1], *inp=BUF;
#define GETCHAR(INP) { \
    if(!*inp) { \
        if (REACHEOF) return 0;\
        memset(BUF,0,sizeof BUF);\
        int inpzzz = fread(BUF,1,BUFSIZE,stdin);\
        if (inpzzz != BUFSIZE) REACHEOF = true;\
        inp=BUF; \
    } \
    INP=*inp++; \
}
#define DIG(a) (((a)>='0')&&((a)<='9'))
#define GN(j) { \
    AM=0;\
    GETCHAR(INP); while(!DIG(INP) && INP!='-') GETCHAR(INP);\
    if (INP=='-') {AM=1;GETCHAR(INP);} \
    j=INP-'0'; GETCHAR(INP); \
    while(DIG(INP)){j=10*j+(INP-'0');GETCHAR(INP);} \
    if (AM) j=-j;\
}
//End of buffer reading

#define TWO(x) (1<<(x))
#define CONTAIN(S,x) (S & TWO(x))

char s[22];
int n;
long double f[TWO(21)];

long double get(int mask) {
	if (mask == 0) return 0;
	if (f[mask] >= 0) return f[mask];
	
	long double res = 0;
	REP(i,n) { // Person arrived at position i
		int j = i, add = n;
		while (!CONTAIN(mask,j)) {
			++j; --add;
			if (j == n) j = 0;
		}
		res += get(mask - TWO(j)) + add;
	}
	res /= n;
	return f[mask] = res;
}

int main() {
    // freopen("input.txt", "r", stdin);
	int ntest; scanf("%d\n", &ntest);
	FOR(test,1,ntest) {
		gets(s);
		n = strlen(s);
		int mask = 0;
		REP(i,n) if (s[i] == '.') mask |= TWO(i);
		
		REP(i,TWO(n)) f[i] = -1;
		
		printf("Case #%d: %.10lf\n", test, (double) get(mask));
	}
    return 0;
}
