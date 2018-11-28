#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std ;
#define rep( i, j, k ) for( i = j ; i <= k ; ++i )
#define Maxn 1015

int T, Case, Ans0, Ans1, n ;
double br[Maxn], ar[Maxn] ;

int main()
{
	int i, j ;
	
	freopen("D_large.in","r",stdin) ;
	freopen("D_large.out","w",stdout) ;
	
	for( scanf("%d", &T) ; T-- ; ) {
		Ans0 = Ans1 = 0 ; 
		
		scanf("%d", &n) ;
		rep( i, 1, n ) scanf("%lf", &ar[i]) ;
		rep( i, 1, n ) scanf("%lf", &br[i]) ;
		
		sort( ar+1, ar+1+n ) ;
		sort( br+1, br+1+n ) ; 
		
	//	rep( i, 1, n ) printf("%.3lf ",ar[i] ) ;
	//	printf("\n") ;
	//	rep( i, 1, n ) printf("%.3lf ", br[i] );
	//	printf("\n") ;
		
		j = 1 ;
		rep( i, 1, n ) {
			while( ( ar[j] < br[i] ) && ( j <= n ) ) ++j ;
			if( j <= n ) {
				++ Ans0 ;
				++ j ;
			} else break ;
		}
		
		j = 1 ;
		rep( i, 1, n ) {
			while( ( br[j] < ar[i] ) && ( j <= n ) ) ++ j ;
			if( j <= n ) ++j ; 
			else {
				Ans1 = n-i+1 ;
				break ;	
			}
		}
		
		printf("Case #%d: %d %d\n", ++Case, Ans0, Ans1 ) ;
	}
//	system("pause") ;
	return 0 ; 
}
