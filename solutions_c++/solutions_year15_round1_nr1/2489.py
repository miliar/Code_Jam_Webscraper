#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cctype>

using namespace std;

#define pb push_back
#define mp make_pair

#define ALL(x) (x).begin(),(x).end()
#define CLR(a,b) memset(a,b,sizeof(a))
#define REPN(x,a,b) for (int x = a; x < b; ++x)
#define REP(x,a,b) for(x = a; x < b; ++x)

#define dbg(x) cout << #x << " = " << x << endl;
#define dbg2(x, y) cout << #x << " = " << x << "  " << #y << " = " << y << endl;
#define dbg3(x, y, z) cout << #x << " = " << x << "  " << #y << " = " << y << "  " << #z << " = " << z << endl;
#define dbg4(x, y, z, w) cout << #x << " = " << x << "  " << #y << " = " << y << "  " << #z << " = " << z << "  " << #w << " = " << w <<  endl;
#define MAXN 1<<28

/* {{{ FAST integer input */
#define X10(n)    ((n << 3) + (n << 1))
#define RdI        readint
const int MAXR = 65536;
char buf[MAXR], *lim = buf + MAXR - 1, *now = lim + 1;
bool adapt(){ // Returns true if there is a number waiting to be read, false otherwise
    while(now <= lim && !isdigit(*now)) ++now;
    if(now > lim){
        int r = fread(buf, 1, MAXR-1, stdin);
        buf[r] = 0;
        lim = buf + r - 1;
        if(r == MAXR - 1){
            while(isdigit(*lim)) ungetc(*lim--, stdin);
            if(*lim == '-') ungetc(*lim--, stdin);
        }
        now = buf;
    }
    while(now <= lim && !isdigit(*now)) ++now;
    return now <= lim;
}
bool readint(int& n){ // Returns true on success, false on failure
    if(!adapt()) return false;
    bool ngtv = *(now - 1) == '-';
    for(n = 0; isdigit(*now); n = X10(n) + *now++ - '0');
    if(ngtv) n = -n;
    return true;
}
/* }}} end FAST integer input */

int A[10001];

int main() {
    int t, cas, n, i, r, s1, s2;
    RdI(t);
    REP(cas, 1, t + 1){
    	RdI(n);
        r = 0;
    	REP(i, 0, n){
            RdI(A[i]);
            if(i > 0 && A[i] < A[i-1]){
                r = max(r, A[i - 1] - A[i]);
            }
        }
        s1 = 0;
        REP(i, 0, n - 1){            
            if(A[i] > A[i + 1])
                s1 += A[i] - A[i + 1];
        }
        /*r = 0;
        if(A[n - 2] > A[n - 1])
            r = A[n - 2] - A[n - 1];*/
        s2 = 0;
        REP(i, 0, n - 1){
            if(A[i] <= r) s2 += A[i];
            else{
                s2 += r;
            }
        }
    	printf("Case #%d: %d %d\n", cas, s1, s2);
    }
	return 0;
}