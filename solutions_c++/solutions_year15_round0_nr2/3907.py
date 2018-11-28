#include <iostream>
#include <fstream>

#define FOR0(i,n) for(i=0;i<n;++i)
#define FOR1(i,n) for(i=1;i<=n;++i)

using namespace std ;

int n, a[2000], k[10], pw10, m, t, ans, ct, cm, i ;

int main() {
    freopen("input.txt","r",stdin) ;
    freopen("output.txt","w",stdout) ;
    int T, _T ;
    cin >> T ;
    FOR1(_T,T) {
        cout << "Case #" << _T << ": " ;

        cin >> n ;

        FOR1(i,n)
            cin >> a[i] ;

        pw10 = 1 ;
        FOR1(i,n)
            pw10 *= 10 ;

        ans = (int)1e9 ;
        FOR0(m,pw10) {
            t = m ; i = 1 ; ct = 0 ; cm = 0 ;
            FOR1(i,n)
                k[i] = 0 ;
            i = 1 ;
            while( t )
                k[i++] = t%10,
                t /= 10 ;
            FOR1(i,n)
                ct += k[i],
                cm = max( cm, (a[i]-1)/(k[i]+1) + 1 ) ;
            ans = min( ans, ct + cm ) ;
        }
        cout << ans << endl ;
    }
}
