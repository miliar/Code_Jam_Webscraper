#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

const int MAXN = 1000 + 100 ;
const int MAXPT = 2000 + 100 ;
const int MAXM = MAXN * MAXN * 10 ;
const long long INF = 2000000100 ;

long long a[ MAXN ] , b[ MAXN ] , pla[ MAXN ] , plb[ MAXN ] ;
int first[ MAXPT ] , last[ MAXM ] , y[ MAXM ] , poww[ MAXM ] ;
int n , lenn , lena , lenb ;
/*
void addd( int a , int b , int p ) {
	last[ lenn ] = first[ a ] ;
	y[ lenn ] = b ;
	poww[ lenn ] = p ;
	first[ a ] = lenn ++ ;
}

void add( int a , int b . int p ) {
	add( a , b , p ) ;
	add( b , a , p ) ; 
}

int dist[ MAXPT ] , que[ MAXPT ] ;

bool bfs( int s , int t ) {
	memset( dist , -1 , sizeof( dist ) ) ;
	int l = 0 , r = 1 ;
	que[ 0 ] = s ;
	while ( l < r ) {
		int pt = que[ l ++ ] ;
		for ( int p = first[ pt ] ; p != -1 ; p = last[ p ] ) 
			if ( dist[ y[ p ] ] == -1 && poww[ p ] > 0 ) {
				que[ r ] = y[ p ] ;
				dist[ y[ p ] ] = dist[ pt ] + 1 ;
				if ( y[ p ] == t ) return true ;
			}
	}
	return false ;
}

int min( int a , int b ) {
	if ( a < b ) return a ;
	return b ;
}

int findpath( int pt , int t , int minn ) {
	if ( pt == t )
		return minn ;
	int cici = 0 ;
	for ( int p = fisrt[ pt ] ; p != -1 ; p = last[ p ] ) {
		if ( dist[ y[ p ] ] == dist[ pt ] + 1 && poww[ p ] > 0 ) {
			int tmp = findpath( y[ p ] , t , min( minn , poww[ p ] ) ) ;
			poww[ p ] -= tmp ;
			poww[ p ^ 1 ] += tmp ; 
			cici += tmp ;
			minn -= tmp ;
		}
	}
	dist[ pt ] = -1 ;
	return cici ;
}
*/

void swap( int&a , int&b ) {
	int t = a ;
	a = b ;
	b = t ;
}

int main() {
	freopen( "B-large.in" , "r" , stdin ) ;
	freopen( "B-large.out" , "w" , stdout ) ;

	int test_case ;
	cin >> test_case ;
	for ( int t = 1 ; t <= test_case ; t ++ ) {
		cin >> n ;
		for ( int i = 0 ; i < n ; i ++ ) {
			cin >> a[ i ] ;
			pla[ i ] = i ; 
		}
		for ( int i = 0 ; i < n ; i ++ )
			for ( int j = i + 1 ; j < n ; j ++ )
				if ( a[ pla[ i ] ] > a[ pla[ j ] ] )
					swap( pla[ i ] , pla[ j ] ) ;

		int ans = 0 ;
		for ( int i = 0 ; i < n ; i ++ ) {
			int x = pla[ i ] ;
			int cici , vivi ;
			cici = x ;
			for ( int j = 0 ; j < x ; j ++ )
				if ( a[ j ] < a[ x ] )
					cici -- ;
			vivi = ( n - x - 1 ) ;
			for ( int j = x + 1 ; j < n ; j ++ )
				if ( a[ j ] < a[ x ] )
					vivi -- ;
			if ( cici < vivi )
				ans += cici ;
			else
				ans += vivi ;
		}

		printf( "Case #%d: %d\n" , t , ans ) ;
		/*
		for ( int i = 0 ; i < n ; i ++ )
			b[ i ] = INF - a[ i ] ;

		memset( first , -1 , sizeof( first ) ) ;
		lenn = 0 ;
		int s = 2 * n , t = s + 1 ;
		for ( int i = 0 ; i < n ; i ++ ) {
			add( s , i , MAXN ) ;
			add( n + i , t , MAXN ) ;
		}
		for ( int i = 0 ; i < n ; i ++ )
			for ( int j = i + 1 ; j < n ; j ++ )
				if ( a[ i ] )

		printf( "Case #%d: %d\n" , t , ans ) ;
		*/
	}
}
