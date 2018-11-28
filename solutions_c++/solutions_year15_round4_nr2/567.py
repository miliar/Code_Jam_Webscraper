/*
 * main.cpp
 *
 *  Created on: 30 ???, 2015 ?.
 *      Author: Tigran
 */



#include <iostream>
#include <iomanip>
#include <vector>
#include <list>
#include <deque>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
#include <iterator>
#include <numeric>
#include <sstream>
#include <cmath>

using std::cin;
using std::cout;
using std::endl;

bool fps_equal( double a, double b )
{
	return fabs( a - b ) <= 0.0000000001;
}

double solve_easy( int N, double V, double X, std::vector< double > R, std::vector< double > C )
{
	if ( N == 1 ) {
		if ( fps_equal( X, C[ 0 ] ) ) {
			return V / R[ 0 ];
		}
		else
			return -1;
	}
	if ( fps_equal( C[ 0 ], C[ 1 ] ) ) {
		if ( fps_equal( X, C[ 0 ] ) ) {
			return V / (R[ 0 ] + R[ 1 ]);
		}
		else
			return -1;
	}
	else {
		double t0 = ( V * (X - C[1]) ) / ( R[0] * (C[0] - C[1]) );
		double t1 = ( V - R[0]*t0 ) / R[1];
		if ( t0 < -0.00000000001 || t1 < -0.00000000001 )
			return -1;
		if ( ! fps_equal( R[0]*t0 + R[1]*t1, V ) )
			return -1;
		if ( ! fps_equal( R[0]*C[0]*t0 + R[1]*C[1]*t1, X*V ) )
			return -1;
		return std::max( t0, t1 );
	}
}

int main()
{
	int TC;
	cin >> TC;
	for ( int tc = 1; tc <= TC; ++tc ) {
		int N;
		double V, X;
		cin >> N;
		cin >> V >> X;
		std::vector< double > R( N ), C( N );
		for ( int i = 0; i < N; ++i )
			cin >> R[ i ] >> C[ i ];
		cout << "Case #" << tc << ": ";
		double r = solve_easy( N, V, X, R, C );
		if ( r < 0 )
			cout << "IMPOSSIBLE";
		else
			cout << std::setiosflags( std::ios::fixed | std::ios::showpoint ) << std::setprecision( 12 ) <<
					r;
		cout << endl;
	}
	return 0;
}

