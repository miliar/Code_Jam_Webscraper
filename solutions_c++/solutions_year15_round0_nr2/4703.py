#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
int a[2000];

int main() {
    int T,step=0;
    
    int N,i ,j,max1,min1,sum;
    
    scanf("%d",&T) ;
    
    while(T--)
	 {
        scanf("%d", &N) ;
        for(i = 0 ; i < N ; i++) 
		{
            scanf("%d", &a[i]) ;
            max1 = max(max1,a[i]) ;
        }
        
        min1 = max1 ;
        
        for(i = 1 ; i <= max1 ; i++) 
		{
            sum = i ;
            for(j = 0 ; j < N ; j++) {
                if( a[j] > i ) {
                    if( a[j]%i == 0 )
                        sum += (a[j]/i-1) ;
                    else
                        sum += (a[j]/i) ;
                }
            }
            min1 = min(min1,sum) ;
        }
        printf("Case #%d: %d\n", ++step, min1) ;
    }
    return 0 ;
}
