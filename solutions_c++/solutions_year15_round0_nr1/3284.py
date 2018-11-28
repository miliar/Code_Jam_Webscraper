#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std ;
#define rep( i, j, k ) for( i = j ; i <= k ; ++i )
#define drep( i, j, k ) for( i = j ; i >= k ; --i ) 
#define Maxn 1015

int T, C, ans, n, ar[Maxn * 10], Case ;
char S[Maxn] ;

int main()
{
	int i, j, tmp  ;
	
	freopen("A-large.in","r", stdin) ;
	freopen("output.txt","w",stdout) ;
	
	for( scanf("%d", &T) ; T-- ; ) {
		C = ans = 0 ;
		
		scanf("%d %s", &n, &S) ;
		rep( i, 0, n ) 
			rep( j, 1, S[i]-'0' )
				ar[++C] = i ;
				
		sort( ar+1, ar+1+C ) ;
		
		tmp = 0 ;
		rep( i, 1, C ) {
			if( ar[i] <= tmp ) 
				tmp ++ ;
			else {
				ans += ( ar[i] - tmp ) ;
				tmp = ar[i] + 1 ;	
			}
		}	
		
		printf("Case #%d: %d\n", ++Case, ans ) ;
	}
	return 0 ;	
}
