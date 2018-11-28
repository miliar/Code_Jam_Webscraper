#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std ;
int diners[1200] ;
int main() {
int TT , stair = 0 ;
int n , i , j , m1 , mn1 , sigma ;
scanf("%d", &TT) ;
while( TT-- ) {
    scanf("%d", &n) ;
    for(i = 0 ; i < n ; i++) {
        scanf("%d", &diners[i]) ;
        m1 = max(m1,diners[i]) ;
    }
    mn1 = m1 ;
    for(i = 1 ; i <= m1 ; i++) {
        sigma = i ;
        for(j = 0 ; j < n ; j++) {
            if( diners[j] > i ) {
                if( diners[j]%i == 0 )
                    sigma += (diners[j]/i-1) ;
                else
                    sigma += (diners[j]/i) ;
            }
        }
        mn1 = min(mn1,sigma) ;
    }
    printf("Case #%d: %d\n", ++stair, mn1) ;
}
    return 0 ;
}
