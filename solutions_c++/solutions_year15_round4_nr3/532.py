//by tzupengwang™
#include<bits/stdc++.h>
using namespace std;

#define FO(it,c) for (__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
typedef long long ll;
typedef pair<int,int> ii;

int n ;
map< string , int > s ;

vector< string > st[ 25 ] ;
vector< int > t[ 25 ] ;

int tim ;
char inn[ 100000 ] ;
void init() {
	tim = 0 ;
	scanf( "%d" , &n ) ;
	gets( inn ) ;
	s.clear() ;
	for ( int i = 0 ; i < n ; i ++ ) {
		st[ i ].clear() ;
		gets( inn ) ;
		istringstream tp( inn ) ;
		string tmp ;
		while ( tp >> tmp ) {
			st[ i ].push_back( tmp ) ;
			if ( !s.count( tmp ) ) s[ tmp ] = tim ++ ;
		}
	}
	for ( int i = 0 ; i < n ; i ++ ) {
		t[ i ].clear() ;
		FO( it , st[ i ] ) t[ i ].push_back( s[ *it ] ) ;
		sort( t[ i ].begin() , t[ i ].end() ) ;
		t[ i ].resize( unique( t[ i ].begin() , t[ i ].end() ) - t[ i ].begin() ) ;
		//FO( it , t[ i ] ) printf( "%d " , *it ) ;
		//puts( "" ) ;
	}
}

int ss[ 1000000 ] ;

void process() {
	int out = 1000000000 ;
	for ( int k = 0 ; k < ( 1 << ( n - 2 ) ) ; k ++ ) {
		for ( int i = 0 ; i < tim ; i ++ ) ss[ i ] = 0 ;
		int ans = 0 ;
		s.clear() ;
		FO( it , t[ 0 ] ) ss[ *it ] += 1 ;
		FO( it , t[ 1 ] ) ss[ *it ] += 2 ;
		for ( int i = 0 ; i < n - 2 ; i ++ ) {
			if ( k & ( 1 << i ) ) {
				FO( it , t[ i + 2 ] ) {
					if ( ss[ *it ] % 2 == 0 ) ss[ *it ] += 1 ;
				}
			} else {
				FO( it , t[ i + 2 ] ) {
					if ( ss[ *it ] < 2 ) ss[ *it ] += 2 ;
				}
			}
		}
		for ( int i = 0 ; i < tim ; i ++ ) if ( ss[ i ] == 3 ) ans ++ ;
		out = min( ans , out ) ;
	}
	cout << out << endl ;
}

int main() {
	int Cases;
	scanf( "%d" , &Cases ) ;
	for ( int cases = 1 ; cases <= Cases ; cases ++ ) {
		init() ;
		printf( "Case #%d: " , cases ) ;
		process() ;
	}
	return 0 ;
}

