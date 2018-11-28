#include <bits/stdc++.h>
using namespace std ;

typedef long long LL ;

#define clr( a , x ) memset ( a , x , sizeof a ) 

const int MAXN = 105 ;

bool a[MAXN] ;
char s[MAXN] ;
int n ;

void solve () {
	scanf ( "%s" , s ) ;
	n = strlen ( s ) ;
	for ( int i = 0 ; i < n ; ++ i ) {
		a[i] = s[i] == '+' ;
	}
	int ans = 0 ;
	for ( int i = n - 1 ; i >= 0 ; -- i ) {
		if ( !a[i] ) {
			++ ans ;
			for ( int j = i ; j >= 0 ; -- j ) {
				a[j] ^= 1 ;
			}
		}
	}
	printf ( "%d\n" , ans ) ;
}

int main () {
	int T ;
	freopen ( "B-large.in" , "r" , stdin ) ;
	freopen ( "B-large.out" , "w" , stdout ) ;
	scanf ( "%d" , &T ) ;
	for ( int i = 1 ; i <= T ; ++ i ) {
		printf ( "Case #%d: " , i ) ;
		solve () ;
	}
	return 0 ;
}