#include <bits/stdc++.h>

using namespace std ;
typedef long long int ll ;
typedef unsigned long long int ull ;
#define dbg(x) cout << #x << ":" << x << endl ;
#define fi(i,a,b) for( i = a ; i <= b ; i++ )
#define fd(i,a,b) for( i = a; i >= b ; i-- )

char str[1000] ;
int main()  {

    #ifndef ONLINE_JUDGE
        freopen( "in.txt" , "r" , stdin ) ;
        freopen( "out.txt" , "w" , stdout ) ;
    #endif // ONLINE_JUDGE

        ll t , p , q , g ;

        cin >> t ;
        for( int k = 1  ;  k <= t ; k++ ) {

            cin >> str ;
            sscanf(str , "%lld/%lld" , &p , &q ) ;
            g = __gcd( p , q) ;
            p /= g ;
            q /= g ;



            cout << "Case #" << k << ": " ;
            if( __builtin_popcount(q) == 1 ){
                    ll counter = 1 ;
                while( 1 ) {
                    if( 2*p < q ) { counter++ ; q /= 2 ;}
                    else { break ; }
                }
                cout << counter << endl ;
            }
            else cout << "impossible" << endl ;

        }

    return 0 ;
}
