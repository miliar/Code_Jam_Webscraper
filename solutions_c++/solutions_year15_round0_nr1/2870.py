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
char s[1010];

int main() {
    freopen( "A.in", "r", stdin );
    freopen( "A.out", "w", stdout );
    
    scanf( "%d", &T );
    int cas = 0;
    while ( T -- ) {
        scanf( "%d %s", &n, s );
        int ret = 0, sum = 0;
        for ( int i = 0; i <= n; i ++ ) {
            int x = (int)s[i] - '0'; 

            if ( sum < i ) {
                ret += i - sum;
                sum = i + x; 
            } else {
                sum += x;
            }
        }
        
        printf( "Case #%d: %d\n", ++cas, ret );
    }
    
    return 0;
}









