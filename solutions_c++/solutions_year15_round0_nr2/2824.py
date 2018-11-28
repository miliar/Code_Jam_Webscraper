#include <stdio.h>
#include <iostream>
#include <string.h>
#include <set>
#include <vector>
#include <algorithm>
using namespace std ;

int m ;

const int N = 1100 ;
int a[N] ;


int main() {
    freopen( "input.txt", "r", stdin ) ;
    freopen( "output2.txt", "w", stdout ) ;
    int T ;
    int cas = 1 ;
    scanf( "%d", &T ) ;
    while ( T-- ) {
        int n ;
        cin >> n ;
        for ( int i = 0; i < n; ++i ) {
            cin >> a[i] ;
            m = max( a[i], m ) ;
        }
        int ret = m ;
        for ( int i = 1; i <= m; ++i ) {
            int t = 0 ;
            for ( int j = 0; j < n; ++j ) {
                int k = (a[j] - 1) / i  ;
                if (k < 0 ) k = 0 ;
                t += k ;
            }

            ret = min( ret, t + i ) ;
        }
        printf("Case #%d: %d\n", cas++, ret ) ;
    }
    return 0 ;
}
