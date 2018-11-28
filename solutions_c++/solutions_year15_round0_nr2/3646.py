#include <cstdio>
    #include <cstring>
    #include <algorithm>
    using namespace std ;
    int a[100000] ;
    int main() {
        int t , step = 0 ;
        int n , i , j , maximum , mininmum , ans ;
        freopen("in.txt","r",stdin) ;
        freopen("out.txt","w",stdout) ;
        scanf("%d", &t) ;
        while( t-- ) {
            scanf("%d", &n) ;
            for(i = 0 ; i < n ; i++) {
                scanf("%d", &a[i]) ;
                maximum = max(maximum,a[i]) ;
            }
            mininmum = maximum ;
            for(i = 1 ; i <= maximum ; i++) {
                ans = i ;
                for(j = 0 ; j < n ; j++) {
                    if( a[j] > i ) {
                        if( a[j]%i == 0 )
                            ans += (a[j]/i-1) ;
                        else
                            ans += (a[j]/i) ;
                    }
                }
                mininmum = min(mininmum,ans) ;
            }
            printf("Case #%d: %d\n", ++step, mininmum) ;
        }
        return 0 ;
    }
