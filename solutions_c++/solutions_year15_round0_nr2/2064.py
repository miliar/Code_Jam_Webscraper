#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std ;

int a[2000] ;
int main() {
    int t , index = 0 ;
    int n , i , j , max1 , min1 , sum ;
    
    freopen("B-large.in","r",stdin) ;
    freopen("B-large.out","w",stdout) ;
    
    scanf("%d", &t) ;
    while( t-- ) {
        scanf("%d", &n) ;
        for(i = 0 ; i < n ; i++) {
            scanf("%d", &a[i]) ;
            max1 = max(max1,a[i]) ;
        }
        min1 = max1 ;
        for(i = 1 ; i <= max1 ; i++) {
            sum = i ;
            //printf("i=%d\n",i);
            for(j = 0 ; j < n ; j++) {
                //printf("j=%d\n",j);
                //printf("a[%d]=%d\n",j,a[j]);
                if( a[j] > i ) {
                    if( a[j]%i == 0 ){
                        //printf("a[j]/i-1 = %d\n",(a[j]/i-1));
                        sum += (a[j]/i-1) ;
                    }
                    else{
                         //printf("a[j]/i = %d\n",(a[j]/i));
                        sum += (a[j]/i) ;
                    }
                }
            }
            //printf("sum=%d\n",sum);
            min1 = min(min1,sum) ;
            //printf("min1=%d\n",min1);
        }
        index++;
        printf("Case #%d: %d\n", index, min1) ;
    }
    return 0 ;
}