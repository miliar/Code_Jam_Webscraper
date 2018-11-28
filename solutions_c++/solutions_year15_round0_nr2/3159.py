#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <queue> 

using namespace std ;
#define rep( i, j, k ) for( i = j ; i <= k ; ++ i ) 
#define drep( i, j, k ) for( i = j ; i >= k ; --i ) 
#define Maxn 1015

int n, ans, Case, T, ar[Maxn];

inline int Check( int p ) 
{
	int re = 0, i ;
	rep( i, 1, n ) 
		re += ((int)((ceil)((double)ar[i]/p))-1) ;
	return re ;
}

int main()
{
	int i, a, tmp, p ;
	
	freopen("B-large.in", "r", stdin) ;
	freopen("output.txt","w",stdout) ;
	
	for(scanf("%d", &T); T-- ; ) { 
		ans = 0 ;
		
		scanf("%d", &n) ;
		rep( i, 1, n ) {
			scanf("%d", &ar[i]) ;
			ans = max( ans, ar[i] ) ;
		}
		
		for( i = 1 ; i <= ans ; ++ i ) 
			ans = min( ans, i + Check( i ) ) ;
		
		printf("Case #%d: %d\n", ++Case, ans) ;

	}
	return 0 ;
}
