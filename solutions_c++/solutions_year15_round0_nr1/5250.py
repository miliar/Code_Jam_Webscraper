#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std ;
int a[10000] ;
int main() {
    int t , step = 0 ;
    int n , i , ans , sum ;
    freopen("A-large.in","r",stdin) ;
    freopen("2.out","w",stdout) ;
    scanf("%d", &t) ;
    while( t-- ) {
        scanf("%d", &n) ;
        for(i = 0 ; i <= n ; i++)
            scanf("%1d", &a[i]) ;
        sum = 0 ;
        ans = 0 ;
        for(i = 0 ; i <= n ; i++){
            if( a[i] == 0 ) continue ;
            if( sum >= i ) {
                sum += a[i] ;
            }
            else {
                ans += (i-sum) ;
                sum += (i-sum+a[i]) ;
            }
        }
        printf("Case #%d: %d\n", ++step, ans ) ;
    }
    return 0 ;
}
