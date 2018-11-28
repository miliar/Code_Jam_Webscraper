#include <stdio.h>
#include <stdlib.h>
#include <sstream>
#include <string.h>
using namespace std;

#define REP(i, n) for(int i=0; i<(n); i++)
#define REPD(i, n) for (int i=(n)-1; i >= 0; i--)
#define FOR(i, a, b) for( int i = a; i <= (b); i++)
#define FORD(i, a, b) for(int i=(a); i >= (b); i--)
#define VAR(a, b) __typeof(b) a=(b)
#define FORCOL(i, col) for(VAR(i, (col).begin()); i!=(col).end(); i++)
#define ZERO(x) memset(x, 0, sizeof x);
#define ALL(x) (x).begin(), (x).end()

#define PB push_back
#define ST first
#define ND second

typedef long long int LL;
typedef long double LD;


bool ARR[1001];

bool isPalin(int number) {
    std::ostringstream ss;
    ss << number;
    const char * n = ss.str().c_str();
    int len = strlen(n);
    REP(i, len>>1) {
        if (n[i] != n[len-1-i]) {
            return false;
        }
    }
    return true;
}

int main() {
    FOR(i, 1, 1000) {
        if (isPalin(i) && isPalin(i*i) && i*i <= 1000) {
            ARR[i*i] = true;
        }
    }
    
    int t;
    scanf("%d\n", &t);
    REP(tt, t) {
        int a, b;
        scanf("%d %d", &a, &b);
        int out = 0;
        FOR(i, a, b) {
            if (ARR[i]) out++;
        }
        printf("Case #%d: %d\n", tt+1, out);
    }
    return 0;
}
