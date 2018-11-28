#include <cstdio>
#include <iostream>
#include <map>
#include <algorithm>
#include <vector>
using namespace std ;
const int MAXN = 10021;
const long long inf = 1000000000000000000LL ;
long long f[MAXN][MAXN] ;
map<int,int> s ;
int a[MAXN] , b[MAXN];
int pos[MAXN] ;
int hashs[MAXN] ;

int main() {
    int T , test = 1 ;

    cin >> T ;
    while ( T-- ) {
        int n ;
        cin >> n ;
        for ( int i = 1 ; i <= n ;++i ) {
            cin >> a[i] ;
            b[i] = a[i] ;
        }
        sort( b+1 , b+n+1 );
        s.clear();
        for ( int i = 1 ; i <= n ; ++i )
            s[ b[i] ] = i ;
        for ( int i = 1 ; i <= n ; ++i ) {
            a[i] = s[ a[i] ] ;
            pos[a[i]] = i ;
        }

        for ( int i = 1 ; i <= n ; ++i ) { hashs[i] = 0 ; }

        long long ans = 0 ;
        for ( int i = 1 ; i <= n ; ++i ) {

            int p = pos[ i ] ;
            int l = 0 , r = 0 ;

            for ( int i = 1 ; i <= n ; ++i )
            if ( i != p )
            {
                if ( hashs[i] == 0 )
                {
                    if ( i < p ) ++ l ;
                    else ++r ;
                }
            }

            ans += min(l,r);
            hashs[p] = 1 ;
        }


        cout << "Case #" << test++ << ": ";
        cout << ans << endl ;

    }

    return 0;
}
