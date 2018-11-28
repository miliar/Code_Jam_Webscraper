#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std ;
const int MAXN = 10001;
int a[MAXN];

int main() {

    int t , n , x ;
    int test = 1 ;

    cin >> t ;
    while ( t-- ) {

        cin >> n >> x ;
        for ( int i = 0 ; i < n ; ++i )
            cin >> a[i] ;
        sort( a , a+n ) ;
        int ans = 0 ;
        for ( int i = 0 , j = n-1 ; i < n && i <= j ; ++i ) {
            while ( a[i] + a[j] > x && i < j ) ++ans , --j ;
            --j ;
            ++ans ;
        }
        cout << "Case #" << test++ << ": " << ans << endl ;
    }


    return 0;
}
