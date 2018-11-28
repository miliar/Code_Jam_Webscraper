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

char cad[100002];
int s = 0;
char _c(char a, char b){
	if(a == '1'){ s = 0; return b; }
	if(b == '1'){ s = 0; return a; }
	if(a == 'i' && b == 'i'){ s = 1; return '1'; }
	if(a == 'i' && b == 'j'){ s = 0; return 'k'; }
	if(a == 'i' && b == 'k'){ s = 1; return 'j'; }
	if(a == 'j' && b == 'i'){ s = 1; return 'k'; }
	if(a == 'j' && b == 'j'){ s = 1; return '1'; }
	if(a == 'j' && b == 'k'){ s = 0; return 'i'; }
	if(a == 'k' && b == 'i'){ s = 0; return 'j'; }
	if(a == 'k' && b == 'j'){ s = 1; return 'i'; }
	if(a == 'k' && b == 'k'){ s = 1; return '1'; }
}

int main() {
    int t, cas, i, X, L, pi, pk, ni, nj, nk;
    bool can;
    char last;
    scanf("%d", &t);
    REP(cas, 1, t+1){
    	scanf("%d%d", &X, &L);
    	scanf("%s", cad);
    	L *= X;
    	for(i = X; i < L; ++i) cad[i] = cad[i - X];
        //printf("%s\n", cad);
    	can = false;
        last = cad[0];
        ni = 0;
        for(i = 1; i < L; ++i){
            if(last == 'i' && !(ni & 1)){
                //printf("yes i %d\n",i);
                last = cad[i++];
                ni = 0;
                for(; i < L; ++i){
                    if(last == 'j' && !(ni & 1)){
                        last = cad[i];
                        ni = 0;
                        //printf("yes j %d %c\n", i, last);
                        for(++i; i < L; ++i){
                            last = _c(last, cad[i]);
                            ni += s;                            
                        }
                        //printf("%c %d\n", last, ni);
                        if(last == 'k' && !(ni & 1) && i == L){
                            //printf("yes k %d\n",i);
                            can = true;
                        }
                    }
                    else{
                        last = _c(last, cad[i]);
                        ni += s;
                    }
                }
            }
            else{
                last = _c(last, cad[i]);
                ni += s;
            }
        }
    	/*pi = pk = -1;
    	i = ni = nk = 0;
    	last = cad[i++];
    	while(i < L && last != 'i'){
    		last = _c(last, cad[i]);
    		ni += s;
    		if(last == 'i' && !(ni & 1)) pi = i;
    		i++;
    	}
    	i = L - 1;
    	last = cad[i--];
    	while(i >= 0 && last != 'k'){
    		last = _c(cad[i], last);
    		nk += s;
    		if(last == 'k' && !(nk & 1)) pk = i;
    		i--;
    	}
    	if(pi >= 0 && pi < L - 2){
    		last = cad[i = pi + 1];
    		nj = 0;
	    	for(++i; i < L; ++i){
	    		if(last == 'j' && !(nj & 1)) break;
	    		else{ last = _c(last, cad[i]); nj += s; }
	    	}
	    	if(i == nk) 
    	}*/
        if(can) printf("Case #%d: YES\n", cas);
        else printf("Case #%d: NO\n", cas);
    }
	return 0;
}