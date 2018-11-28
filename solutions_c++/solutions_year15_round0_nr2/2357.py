#include<bits/stdc++.h>


using namespace std ;

int main() {
    int t , tc = 1 ,a[1006];
    int n , i , j , mx , res , sum=0 ;
    freopen("B-large.in","r",stdin) ;
    freopen("2.outlarge.txt","w",stdout) ;
    scanf("%d", &t) ;
    while( t-- ) {
        scanf("%d", &n) ;
        for(i = 0 ; i < n ; i++) {
            scanf("%d", &a[i]) ;
            mx = max(mx,a[i]) ;
        }
        res = mx ;
        for(i = 1 ; i <= mx ; i++) {
            sum = i ;
            for(j = 0 ; j < n ; j++) {
                if( a[j] > i ) {
                    if( a[j]%i == 0 )
                        sum += (a[j]/i-1) ;
                    else
                        sum += (a[j]/i) ;
                }
            }
            res = min(res,sum) ;
        }
        printf("Case #%d: %d\n", tc++, res) ;
    }
    return 0 ;
}
