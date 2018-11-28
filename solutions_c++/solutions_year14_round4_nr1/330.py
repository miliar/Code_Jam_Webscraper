#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cstring>

using namespace std ;
#define drep( i, j, k ) for( i = j ; i >= k ; --i )
#define rep( i, j, k ) for( i = j ; i <= k ; ++i )
#define Maxn 10015

int T, n, X, ans, P, Case ; 
int ar[Maxn] ;

int main()
{
	int i ;
	
	freopen("A-large.in","r",stdin) ;
	freopen("A.out","w",stdout) ;
	
	for( scanf("%d", &T) ; T-- ; ) {
		ans = 0 ;
		
		scanf("%d%d", &n, &X) ;
		rep( i, 1, n ) 
			scanf("%d", &ar[i]) ;
		
		sort( ar+1, ar+1+n ) ; 	
		
		P = 1 ; 
		for( i = n ; i >= P ; --i ) {
			if( i == P ) {
				++ ans ;
				break ;	
			}
			if( ar[i] + ar[P] <= X ) {
				++ ans ;
				++ P ;	
			} else ++ ans ;
		}
		
		printf("Case #%d: %d\n", ++ Case, ans) ;
	}
	return 0 ; 
}
