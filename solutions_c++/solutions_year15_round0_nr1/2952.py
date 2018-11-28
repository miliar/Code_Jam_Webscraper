#include <stdio.h>
#include <iostream>
#include <string.h>

using namespace std ;

const int N = 1100 ;
int n ;
char s[N] ;

int main() {
    freopen( "input.txt", "r", stdin ) ;
    freopen( "output.txt", "w", stdout ) ;
    int T, cas = 1 ;
    cin >> T ;
    while ( T-- ) {
        cin >> n ;
        int ret = 0 ;
        cin >> s ;
        int now = 0 ;
        for ( int i = 0; i <= n; ++i ) {
            int cnt = s[i] - '0' ;
            if ( now < i ) {
                ret += i - now ;
                now = i ;
            }
            now += cnt ;
        }
        cout << "Case #" << cas++ << ": " << ret << endl ;
    }
    return 0 ;
}
