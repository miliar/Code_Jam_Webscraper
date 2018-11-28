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

int n ;
char s[MAXN] ;

void solve () {
	int ans = 0 , sum = 0 ;
	scanf ( "%d%s" , &n , s ) ;
	sum += s[0] - '0' ;
	For ( i , 1 , n ) {
		int x = s[i] - '0' ;
		if ( i > sum && x ) {
			ans += i - sum ;
			sum += i - sum ;
		}
		sum += x ;
	}
	printf ( "%d\n" , ans ) ;
}

int main () {
	int T ;
	freopen ( "A-large.in" , "r" , stdin ) ;
	freopen ( "A-large.out" , "w" , stdout ) ;
	scanf ( "%d" , &T ) ;
	For ( i , 1 , T ) {
		printf ( "Case #%d: " , i ) ;
		solve () ;
	}
	return 0 ;
}