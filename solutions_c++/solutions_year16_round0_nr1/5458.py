#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstring>
#include <cctype>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define VAR(a,b)        __typeof(b) a=(b)
#define REP(i,n)        for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b)      for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b)     for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c)   for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(c)          (c).begin(),(c).end()
#define TRACE(x)        cerr << "TRACE(" #x ")" << endl;
#define DEBUG(x)        cerr << #x << " = " << x << endl;
#define eprintf(...)    fprintf(stderr, __VA_ARGS__)

typedef long long               ll;
typedef long double             ld;
typedef unsigned long           ulong;
typedef unsigned long long      ull;
typedef vector<int>             VI;
typedef vector<char>            VC;

char a[10];

int main() {
    //freopen("input",  "r", stdin);
    //freopen("output", "w", stdout);
    int TN, N;
    cin >> TN;
    FOR(TI,1,TN) {
        cin >> N;
        memset(a, 0, sizeof(a));
        bool done;
        FOR(I,1,99999) {
            ll K = (ll)N * (ll)I;
            while (K > 0) {
                a[K % 10] = true;
                K /= 10;
            }
            done = true;
            FOR(i,0,9)
                done = done && a[i];
            if (done) {
                printf("Case #%d: %lld\n", TI, ((ll)I*(ll)N));
                break;
            }                          
        }
        if (!done)
            printf("Case #%d: INSOMNIA\n", TI);
    } // next test
    return 0;
}
