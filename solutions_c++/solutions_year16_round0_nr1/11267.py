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
#define MAXN 100001

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

typedef unsigned long long int ull;

int M[MAXN][11];

set<int> _digits(int n){
    set<int> v;
    int r;
    while(n > 9){
        r = n%10;
        v.insert(r);
        n /= 10;
    }
    v.insert(n);
    return v;
}

vector<int> _divisors(int n){
    int i = 1;
    vector<int> v;
    while(i <= sqrt(n)) {
        if(n%i == 0) {
            v.pb(i);
            if (i != (n / i)) {
                v.pb(n / i);
            }
        }
        i++;
    }
    return v;
}

void _process(){
    int i, j;
    REP(i, 1, MAXN){
        set<int> m = _digits(i);
        vector<int> v = _divisors(i);
        REP(j, 0, v.size()){
            set<int>::iterator d;
            for(d = m.begin(); d != m.end(); ++d ){
                if(!M[v[j]][*d]){
                    M[v[j]][*d] = i;
                    M[v[j]][10]++;
                }
            }
        }
    }
}

int main() {
    int cas, n, t, i, g;
    scanf("%d", &t);
    t++;
    _process();
    REP(cas, 1, t){
        scanf("%d", &n);
        if(M[n][10] == 10){
            g = 0;
            REP(i, 0, 10){
                if(M[n][i] > g) g = M[n][i]; 
            }
            printf("Case #%d: %d\n", cas, g);
        }
        else printf("Case #%d: INSOMNIA\n", cas);
    }
    /*std::vector<int> v = _divisors(24);
    REPN(i, 0, 11){
        printf("%d - ", v[i]);
    }*/
    return 0;
}
