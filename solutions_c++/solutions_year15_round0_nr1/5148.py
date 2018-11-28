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

char cad[1002];

int main() {
    int t, cas, i, n, l, acum, f;
    scanf("%d", &t);
    REP(cas, 1, t+1){
    	scanf("%d", &n);
    	scanf("%s", cad);
    	acum = (cad[f = i = 0] & 15);
    	while(cad[++i]){
    		if(acum >= i) acum += (cad[i] & 15);
    		else{
    			f += i - acum;
    			acum += i - acum + (cad[i] & 15);
    		}
    	}
    	printf("Case #%d: %d\n", cas, f);
    }
	return 0;
}