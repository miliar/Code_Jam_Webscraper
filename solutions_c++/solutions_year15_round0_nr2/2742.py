#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
using namespace std;
#define SZ(v) ((int)(v).size())
#define REP(i, n) for (int i = 0; i < (n); ++i)
#define REPF(i, a, b) for (int i = (a); i <= (b); ++i)
#define REPD(i, a, b) for (int i = (a); i >= (b); --i)
const int maxint = -1u>>1;
int T, n;
int p[1010];

int calc( int x ) {
    int ret = 0;
    for ( int i = 1; i <= n; i ++ ) {
        ret += ( p[i] + x - 1 ) / x - 1;
    }
    return ret;
}

int main() {
    freopen( "input.in", "r", stdin );
    freopen( "B.out", "w", stdout );
    
    scanf( "%d", &T );
    for ( int cas = 1; cas <= T; cas ++ ) {
        scanf( "%d", &n );
        for ( int i = 1; i <= n; i ++ ) {
            scanf( "%d", &p[i] );
        }

        int ret = 1010;
        for ( int i = 1; i <= 1000; i ++ ) {
            ret = min( ret, calc( i ) + i );
        }

        printf( "Case #%d: %d\n", cas, ret );
    }
    
    return 0;
}










