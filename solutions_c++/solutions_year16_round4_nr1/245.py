#include <bits/stdc++.h>
using namespace std ;

int n , R , P , S ;
string s[1 << 13] ;
string ans ;

char encode ( int v ) {
	if ( v == 0 ) return 'P' ;
	if ( v == 1 ) return 'S' ;
	return 'R' ;
}

void dfs ( int cur , int v , int o ) {
	if ( cur == n ) {
		s[o] = encode ( v ) ;
		return ;
	}
	dfs ( cur + 1 , v , o << 1 ) ;
	dfs ( cur + 1 , ( v + 2 ) % 3 , o << 1 | 1 ) ;
	if ( s[o << 1] < s[o << 1 | 1] ) s[o] = s[o << 1] + s[o << 1 | 1] ;
	else s[o] = s[o << 1 | 1] + s[o << 1] ;
}

void calc ( int v ) {
	int a = 0 , b = 0 , c = 0 ;
	dfs ( 0 , v , 1 ) ;
	for ( int i = 0 ; i < s[1].size () ; ++ i ) {
		if ( s[1][i] == 'R' ) ++ a ;
		if ( s[1][i] == 'P' ) ++ b ;
		if ( s[1][i] == 'S' ) ++ c ;
	}
	if ( a != R || b != P || c != S ) return ;
	if ( !ans.size () || ans > s[1] ) ans = s[1] ;
}

void solve () {
	ans = "" ;
	scanf ( "%d%d%d%d" , &n , &R , &P , &S ) ;
	calc ( 0 ) ;
	calc ( 1 ) ;
	calc ( 2 ) ;
	if ( !ans.size () ) {
		printf ( "IMPOSSIBLE\n" ) ;
		return ;
	}
	for ( int i = 0 ; i < ans.size () ; ++ i ) {
		printf ( "%c" , ans[i] ) ;
	}
	puts ( "" ) ;
}

int main () {
	int T ;
	freopen ( "A-large.in" , "r" , stdin ) ;
	freopen ( "A-large.out" , "w" , stdout ) ;
	scanf ( "%d" , &T ) ;
	for ( int i = 1 ; i <= T ; ++ i ) {
		printf ( "Case #%d: " , i ) ;
		solve () ;
	}
	return 0 ;
}