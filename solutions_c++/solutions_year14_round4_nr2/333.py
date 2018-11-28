#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <algorithm>

using namespace std ;
#define rep( i, j, k ) for( i = j ; i <= k ; ++i )
#define drep( i, j, k ) for( i = j ; i >= k ; --i )
#define Maxn 10015

int T, n, ar[Maxn], ans, P0, P1, Case ;

int main()
{
	int i, j, t ;
	
	freopen("B-large.in","r",stdin) ;
	freopen("B.out","w",stdout) ;
	
	for( scanf("%d", &T) ; T-- ; ) {
		ans = 0 ;
		
		scanf("%d", &n) ;
		rep( i, 1, n ) 
			scanf("%d", &ar[i]) ;
			
		P0 = 1, P1 = n ; 
		rep( i, 1, n ) {
			t = P0 ;
			rep( j, P0, P1 ) 
				if( ar[j] < ar[t] ) 
					t = j ; 
			
			if( abs( t - P0 ) < abs( t - P1 ) ) {
				drep( j, t-1, P0 ) {
					swap( ar[j+1], ar[j] ) ;
					++ ans ;
				}
				++ P0 ;
			} else {
				rep( j, t+1, P1 ) {
					swap( ar[j-1], ar[j] ) ;
					++ ans ;	
				}	
				-- P1 ;
			}
		}
		
		printf("Case #%d: %d\n", ++ Case, ans) ;
			
	}
	
	return 0 ; 	
}
