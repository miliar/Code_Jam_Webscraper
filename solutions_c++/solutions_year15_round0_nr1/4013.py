#include <iostream>
#include <fstream>

#define FOR0(i,n) for(i=0;i<n;++i)
#define FOR1(i,n) for(i=1;i<=n;++i)

using namespace std ;

int cnt, ans, i, d, L ; char c ;

int main() {
    freopen("input.txt","r",stdin) ;
    freopen("output.txt","w",stdout) ;
    int T, _T ;
    cin >> T ;
    FOR1(_T,T) {
        cnt = ans = 0 ;
        cin >> L ;
        FOR0(i,L+1) {
            cin >> c ;
            if( c > '0' && i > cnt ) {
                d = i-cnt ;
                ans += d ;
                cnt += d ;
            }
            cnt += c-'0' ;
        }
        cout << "Case #" << _T << ": " ;
        cout << ans << endl ;
    }
}
