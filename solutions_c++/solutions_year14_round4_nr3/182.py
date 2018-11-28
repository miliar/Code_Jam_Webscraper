#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

const int MAXN = 1000 + 100 ;

int x1[ MAXN ] , y1[ MAXN ] , x2[ MAXN ] , y2[ MAXN ] ;
long long g[ MAXN ] [ MAXN ] ;
int w , h , n ;

int abs( int x ) {
	if ( x < 0 ) return -x ;
	return x ;
}

int minn( int a , int b ) {
	if ( a < b ) return a ;
	return b ;
}

int maxx( int a , int b ) {
	if ( a > b ) return a ;
	return b ; 
}

int getdist( int x1 , int y1 , int x2 , int y2 , int x , int y ) {
	int cici = maxx( abs( x1 - x ) , abs( y1 - y ) ) - 1 ;
	cici = minn( cici , maxx( abs( x1 - x ) , abs( y2 - y ) ) - 1 ) ;
	cici = minn( cici , maxx( abs( x2 - x ) , abs( y2 - y ) ) - 1 ) ;
	cici = minn( cici , maxx( abs( x2 - x ) , abs( y1 - y ) ) - 1 ) ;
	return cici ;
}

long long dist[ MAXN ] ;
bool use[ MAXN ] ;

int main() {
	// freopen( "C.in" , "r" , stdin ) ;
	freopen( "C-large.in" , "r" , stdin ) ;
	freopen( "C-large.out" , "w" , stdout ) ;

	int test_case ;
	cin >> test_case ;
	for ( int t = 1 ; t <= test_case ; t ++ ) {
		cin >> w >> h >> n ;
		for ( int i = 0 ; i < n ; i ++ )
			cin >> x1[ i ] >> y1[ i ] >> x2[ i ] >> y2[ i ] ;
		int st = n , ed = n + 1 ;
		for ( int i = 0 ; i < n ; i ++ ) {
			g[ st ] [ i ] = g[ i ] [ st ] = x1[ i ] ;
			g[ i ] [ ed ] = g[ ed ] [ i ] = w - x2[ i ] - 1 ;
		}
		g[ st ] [ ed ] = g[ ed ] [ st ] = w ;
		for ( int i = 0 ; i < n ; i ++ )
			for ( int j = 0 ; j < n ; j ++ ) if ( i != j ) {
				g[ i ] [ j ] = getdist( x1[ i ] , y1[ i ] , x2[ i ] , y2[ i ] , x1[ j ] , y1[ j ] ) ;
				g[ i ] [ j ] = minn( g[ i ] [ j ] , getdist( x1[ i ] , y1[ i ] , x2[ i ] , y2[ i ] , x1[ j ] , y2[ j ] ) ) ;
				g[ i ] [ j ] = minn( g[ i ] [ j ] , getdist( x1[ i ] , y1[ i ] , x2[ i ] , y2[ i ] , x2[ j ] , y1[ j ] ) ) ;
				g[ i ] [ j ] = minn( g[ i ] [ j ] , getdist( x1[ i ] , y1[ i ] , x2[ i ] , y2[ i ] , x2[ j ] , y2[ j ] ) ) ;
				if ( y1[ i ] <= y2[ j ] && y2[ i ] >= y1[ j ] ) {
					g[ i ] [ j ] = minn( g[ i ] [ j ] , getdist( x1[ i ] , y1[ i ] , x2[ i ] , y2[ i ] , x1[ j ] , y1[ i ] ) ) ;
					g[ i ] [ j ] = minn( g[ i ] [ j ] , getdist( x1[ i ] , y1[ i ] , x2[ i ] , y2[ i ] , x2[ j ] , y1[ i ] ) ) ;
				}
				if ( x1[ i ] <= x2[ j ] && x2[ i ] >= x1[ j ] ) {
					g[ i ] [ j ] = minn( g[ i ] [ j ] , getdist( x1[ i ] , y1[ i ] , x2[ i ] , y2[ i ] , x1[ i ] , y1[ j ] ) ) ;
					g[ i ] [ j ] = minn( g[ i ] [ j ] , getdist( x1[ i ] , y1[ i ] , x2[ i ] , y2[ i ] , x1[ i ] , y2[ j ] ) ) ;
				}
			}
			/*
		for ( int i = 0 ; i <= n + 1 ; i ++ ) {
			for ( int j = 0 ; j <= n + 1 ; j ++ )
				cout << g[ i ] [ j ] << ' ' ;
			cout << endl;
		}*/
		memset( dist , -1 , sizeof( dist ) ) ;
		memset( use , true , sizeof( use ) ) ;
		dist[ st ] = 0 ;
		while ( true ) {
			long long m = -1 ; int p = -1 ;
			for ( int i = 0 ; i <= ed ; i ++ )
				if ( dist[ i ] != -1 && use[ i ] && ( p == - 1 || dist[ i ] < m ) ) {
					m = dist[ i ] ;
					p = i ;
				}
			if ( p == -1 ) 
				break ;
			use[ p ] = false ;
			for ( int i = 0 ; i <= ed ; i ++ )
				if ( dist[ i ] == -1 || dist[ p ] + g[ p ] [ i ] < dist[ i ] )
					dist[ i ] = dist[ p ] + g[ p ] [ i ] ;
		}
		printf( "Case #%d: %lld\n" , t , dist[ ed ] ) ;
	}
}
