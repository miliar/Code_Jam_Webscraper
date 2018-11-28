#include<stdio.h>
#include<limits.h>
using namespace std ;
  
int a[1200] ;

int min(int a , int b)
{
		return(a<b?a:b);
} 

int max(int a , int b)
{
	return(a>b?a:b);
 } 
int main()
 {  
    int t , counter = 1 ;  
    int d , i , j , maximum , minimum , result ; 
	maximum = INT_MIN; 
    scanf("%d", &t) ;  
    while( t-- ) {  
        scanf("%d", &d) ;  
        for(i = 0 ; i < d ; i++) {  
            scanf("%d", &a[i]) ;  
            maximum = max(maximum,a[i]) ;  
        }  
        minimum = maximum ;  
        for(i = 1 ; i <= maximum ; i++) {  
            result = i ;  
            for(j = 0 ; j < d ; j++) {  
                if( a[j] > i ) {  
                    if( a[j]%i == 0 )  
                        result += (a[j]/i-1) ;  
                    else  
                        result += (a[j]/i) ;  
                }  
            }  
            minimum = min(minimum,result) ;  
        }  
        printf("Case #%d: %d\n", counter++, minimum) ;  
    }  
    return 0 ;  
}  
