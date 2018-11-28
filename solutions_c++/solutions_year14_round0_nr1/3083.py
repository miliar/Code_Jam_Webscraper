#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std ;
#define rep( i, j, k ) for( i = j ; i <= k ; ++i ) 
#define Maxn 25

int Ans, Case, n, C[Maxn] ;
int main()
{
	int t, T, i, j, a ;
	
	freopen("A_small.in","r",stdin) ;
	freopen("A_small.out","w",stdout) ;
	
	for( scanf("%d", &T ) ; T-- ; ) {
		Ans = 0;
		memset( C, 0, sizeof( C ) ) ;
		
		rep( t, 0, 1 ) {
			scanf("%d", &n) ;
			rep( i, 1, 4 )
				rep( j, 1, 4 ) {
					scanf("%d", &a) ;
					if( i == n ) 
						++ C[a] ; 	
				}
		}
		rep( i, 1, 16 ) 
			if( C[i] == 2 ) 
				++ Ans ;
		
		printf("Case #%d: ", ++Case) ;
		if( Ans == 0 ) 
			printf("Volunteer cheated!\n") ;
		else if( Ans > 1 ) 
			printf("Bad magician!\n") ;
		else {
			rep( i, 1, 16 )
				if( C[i] == 2 )
					printf("%d\n",i) ;	
		}	
	}
//	system("pause") ;
	return 0 ; 	
}
