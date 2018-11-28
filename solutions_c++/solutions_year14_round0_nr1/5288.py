#include <cstdio>
#include <cstring>

using namespace std ;

int main() {
    freopen("A-small-attempt1.in" , "r" , stdin ) ;
    freopen("A.out" , "w" , stdout ) ;
    int num1[4] , num2[4] , step = 0 ;
    int T ; scanf("%d" , &T ) ;
    while( T -- ) {
        int a , b ;
        scanf("%d" , &a ) ;
        for( int i = 1 ; i <= 4 ; i ++ ) {
            if( i == a ) {
                scanf("%d%d%d%d" , &num1[0] , &num1[1] , &num1[2] , &num1[3] ) ;
            }
            else scanf("%*d%*d%*d%*d") ;
        }
        scanf("%d" , &b ) ;
        for( int i = 1 ; i <= 4 ; i ++ ) {
            if( i == b ) {
                scanf("%d%d%d%d" , &num2[0] , &num2[1] , &num2[2] , &num2[3] ) ;
            }
            else scanf("%*d%*d%*d%*d") ;
        }
        int ans = 0 , num = 0 ;
        for( int i = 0 ; i < 4 ; i ++ ) {
            for( int j = 0 ; j < 4 ; j ++ ) {
                if( num1[i] == num2[j] ) {
                    num += 1 ;
                    ans = num1[i] ;
                }
            }
        }
        printf("Case #%d: " , ++ step ) ;
        if( num == 0 ) printf("Volunteer cheated!\n") ;
        else if( num == 1 ) printf("%d\n" , ans ) ;
        else printf("Bad magician!\n") ;
    }

    return 0 ;
}
