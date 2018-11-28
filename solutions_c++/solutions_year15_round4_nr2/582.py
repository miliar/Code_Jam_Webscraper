//by tzupengwang™
#include<bits/stdc++.h>
using namespace std;

#define FO(it,c) for (__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
typedef long long ll;
typedef pair<double,double> ii;

const int T = 80 ;
const double eps = 1e-9 ;
int n ;
double v , x ;
struct ms {
	double r , c ;
	bool operator <( const ms &x ) {
		return c + eps < x.c ;
	}
} s[ 105 ] ;

void init() {
	cin >> n >> v >> x ;
	for ( int i = 0 ; i < n ; i ++ ) {
		cin >> s[ i ].r >> s[ i ].c ;
	}
	sort( s , s + n ) ;
}

bool ok( double now ) {
	//cout << now << endl ;
	double left = v , low = 0 , high = 0 ;
	for ( int i = 0 ; i < n ; i ++ ) {
		if ( left > eps ) {
			if ( s[ i ].r * now > left ) {
				//cout << "in\n" ;
				low += left * s[ i ].c ;
				left = 0 ;
			} else {
				left -= s[ i ].r * now ;
				low += s[ i ].r * now * s[ i ].c ;
			}
		} else break ;
	}
	//cout << low << endl ;
	if ( left > eps ) return false ;
	left = v ;
	for ( int i = n - 1 ; i >= 0 ; i -- ) {
		if ( left > eps ) {
			if ( s[ i ].r * now > left ) {
				high += left * s[ i ].c ;
				left = 0 ;
			} else {
				left -= s[ i ].r * now ;
				high += s[ i ].r * now * s[ i ].c ;
			}
		} else break ;
	}
	//cout << high << endl ;
	if ( low < ( v * x ) + eps && high > ( v * x ) - eps ) return true ;
	return false ;
}

void process() {
	if ( n == 1 ) {
		if ( s[ 0 ].c == x ) printf( "%.15f\n" , v / s[ 0 ].r ) ;
		else puts( "IMPOSSIBLE" ) ;
	} else if ( s[ 1 ].c < x - eps ) puts( "IMPOSSIBLE" ) ;
	else if ( s[ 0 ].c > x + eps ) puts( "IMPOSSIBLE" ) ;
	else {
		double ans ;
		if ( s[ 0 ].c == s[ 1 ].c ) ans = v / ( s[ 0 ].r + s[ 1 ].r ) ;
		else {
			ans = max( v * ( x - s[ 0 ].c ) / ( ( s[ 1 ].c - s[ 0 ].c ) * s[ 1 ].r ) , v * ( x - s[ 1 ].c ) / ( ( s[ 0 ].c - s[ 1 ].c ) * s[ 0 ].r ) ) ;
		}
			printf( "%.15f\n" , ans ) ;
	}
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


