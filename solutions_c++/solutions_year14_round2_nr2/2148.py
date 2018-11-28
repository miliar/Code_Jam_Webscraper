#include <bits/stdc++.h>

using namespace std ;

int main() {

    int t , a , b , k , counter ;

    #ifndef ONLINE_JUDGE
        freopen("in.txt" , "r" , stdin) ;
        freopen(  "out.txt" , "w" , stdout ) ;
    #endif // ONLINE_JUDGE
    cin >> t ;
    for( int l = 1 ; l <= t ; l++ ) {

            counter = 0 ;
            cin >> a >> b >> k ;
        for( int i = 0 ; i < a ; i++ )
            for( int j = 0 ; j < b ; j++ )
                if( (i&j) < k )  counter++ ;

        cout << "Case #" << l << ": " ;
        cout << counter << endl ;

    }
    return 0 ;
}
