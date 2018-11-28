/*
 * B.cpp
 *
 *  Created on: May 28, 2016
 *      Author: tigran
 */



#include <iostream>
#include <sstream>
#include <vector>
#include <list>
#include <deque>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <iterator>
#include <functional>
#include <string>
#include <cassert>
#include <iomanip>

using namespace std;

double calc_probability( const vector< double >& p )
{
	int n = p.size();
	assert( n % 2 == 0 );
	vector< vector< double > > m( n + 1, vector< double >( n + 1 ) );
	m[ 0 ][ 0 ] = 1.0;
	for ( int sel = 1; sel <= n; ++sel )
		m[ sel ][ 0 ] = m[ sel - 1 ][ 0 ] * (1.0 - p[ sel - 1 ] );
	for ( int k = 1; k <= n; ++k )
		m[ 0 ][ k ] = 0.0;
	for ( int sel = 1; sel <= n; ++sel ) {
		for ( int k = 1; k <= sel; ++k ) {
			m[ sel ][ k ] = m[ sel - 1 ][ k ] * (1.0 - p[ sel - 1 ]) +
					m[ sel - 1 ][ k - 1 ] * p[ sel - 1 ];
		}
	}
	return m[ n ][ n / 2 ];
}

void solve_small()
{
	int N, K;
	cin >> N >> K;
	assert( K % 2 == 0 );
	vector< double > p( N );
	for ( int i = 0; i < N; ++i )
		cin >> p[ i ];
	double result = 0.0;
	for ( int k = 0; k < (1 << N); ++k ) {
		vector< double > ps;
		for ( int i = 0; i < N; ++i )
			if ( k & (1 << i) )
				ps.push_back( p[ i ] );
		if ( ps.size() < 2 )
			continue;
		if ( ps.size() % 2 == 1 )
			continue;
		if ( (int)ps.size() != K )
			continue;
		result = max( result, calc_probability( ps ) );
	}
	cout << setiosflags( ios::fixed | ios::showpoint ) << setprecision( 8 ) <<
			result << endl;
}

void solve()
{
	int N, K;
	cin >> N >> K;
	assert( K % 2 == 0 );
	vector< double > p( N );
	for ( int i = 0; i < N; ++i )
		cin >> p[ i ];
	sort( p.begin(), p.end() );
	double result = 0.0;
	for ( int kk = 0; kk <= K; ++kk ) {
		vector< double > ps;
		ps.insert( ps.end(), p.begin(), p.begin() + kk );
		ps.insert( ps.end(), p.end() - (K - kk), p.end() );
		result = max( result, calc_probability( ps ) );
	}
	cout << setiosflags( ios::fixed | ios::showpoint ) << setprecision( 8 ) <<
			result << endl;
}

int main()
{
	int TC;
	cin >> TC;
	for ( int tc = 1; tc <= TC; ++tc ) {
		cout << "Case #" << tc << ": ";
		solve();
	}
	return 0;
}

