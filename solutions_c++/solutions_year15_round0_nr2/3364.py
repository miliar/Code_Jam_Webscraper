#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std ;
int a[1200] ;
int main() {
    int test_cases , count = 0 ;
    int n , i , j , maximum , minimum , sums ;
    freopen("B-small-attempt1.in","r",stdin) ;
    freopen("B-out.txt","w",stdout) ;
    scanf("%d", &test_cases) ;
    while( test_cases-- ) {
        scanf("%d", &n) ;
        for(i = 0 ; i < n ; i++) {
            scanf("%d", &a[i]) ;
            maximum = max(maximum,a[i]) ;
        }
        minimum = maximum ;
        for(i = 1 ; i <= maximum ; i++) {
            sums = i ;
            for(j = 0 ; j < n ; j++) {
                if( a[j] > i ) {
                    if( a[j]%i == 0 )
                        sums += (a[j]/i-1) ;
                    else
                        sums += (a[j]/i) ;
                }
            }
            minimum = min(minimum,sums) ;
        }
        printf("Case #%d: %d\n", ++count, minimum) ;
    }
    return 0 ;
}
