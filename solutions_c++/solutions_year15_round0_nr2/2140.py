#include <cstdio>
#include <cstring>
#include <map>
#include <math.h>
#include <algorithm>
using namespace std ;

typedef long long LL ;

#define rep( i , a , b ) for ( int i = ( a ) ; i <  ( b ) ; ++ i )
#define For( i , a , b ) for ( int i = ( a ) ; i <= ( b ) ; ++ i )
#define rev( i , a , b ) for ( int i = ( a ) ; i >= ( b ) ; -- i )
#define clr( a , x ) memset ( a , x , sizeof a )

const int MAXN = 1005 ;
const int INF = 0x3f3f3f3f ;

int n ;
int d[MAXN] ;

void solve () {
	scanf ( "%d" , &n ) ;
	For ( i , 1 , n ) scanf ( "%d" , &d[i] ) ;
	sort ( d + 1 , d + n + 1 ) ;
	int ans = INF ;
	rev ( i , d[n] , 1 ) {
		int step = 0 ;
		rev ( j , n , 1 ) {
			if ( d[j] > i ) {
				step += ( d[j] - 1 ) / i ;
			} else break ;
		}
		//printf ( "%d %d\n" , step , i ) ;
		ans = min ( ans , step + i ) ;
	}
	printf ( "%d\n" , ans ) ;
}

int main () {
	int T ;
	freopen ( "B-large.in" , "r" , stdin ) ;
	freopen ( "B-large.out" , "w" , stdout ) ;
	scanf ( "%d" , &T ) ;
	For ( i , 1 , T ) {
		printf ( "Case #%d: " , i ) ;
		solve () ;
	}
	return 0 ;
}