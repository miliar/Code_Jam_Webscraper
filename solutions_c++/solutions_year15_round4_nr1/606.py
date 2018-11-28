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

int solve( int R, int C, std::vector< std::vector< char > >& m )
{
	std::vector< int > count_on_row( R, 0 );
	std::vector< int > count_on_column( C, 0 );
	for ( int r = 0; r < R; ++r ) {
		for ( int c = 0; c < C; ++c ) {
			if ( m[ r ][ c ] != '.' ) {
				++count_on_row[ r ];
				++count_on_column[ c ];
			}
		}
	}
	for ( int r = 0; r < R; ++r ) {
		for ( int c = 0; c < C; ++c ) {
			if ( m[ r ][ c ] != '.' ) {
				if ( count_on_row[ r ] == 1 && count_on_column[ c ] == 1 )
					return -1;
			}
		}
	}
	int result = 0;
	for ( int r = 0; r < R; ++r ) {
		for ( int c = 0; c < C; ++c ) {
			if ( m[ r ][ c ] != '.' ) {
				if ( m[ r ][ c ] == '<' )
					++result;
				break;
			}
		}
	}
	for ( int r = 0; r < R; ++r ) {
		for ( int c = C - 1; c >= 0; --c ) {
			if ( m[ r ][ c ] != '.' ) {
				if ( m[ r ][ c ] == '>' )
					++result;
				break;
			}
		}
	}
	for ( int c = 0; c < C; ++c ) {
		for ( int r = 0; r < R; ++r ) {
			if ( m[ r ][ c ] != '.' ) {
				if ( m[ r ][ c ] == '^' )
					++result;
				break;
			}
		}
	}
	for ( int c = 0; c < C; ++c ) {
		for ( int r = R - 1; r >= 0; --r ) {
			if ( m[ r ][ c ] != '.' ) {
				if ( m[ r ][ c ] == 'v' )
					++result;
				break;
			}
		}
	}
	return result;
}

int main()
{
	int TC;
	cin >> TC;
	for ( int tc = 1; tc <= TC; ++tc ) {
		int R, C;
		cin >> R >> C;
		std::vector< std::vector< char > > m( R, std::vector< char >( C ) );
		for ( int r = 0; r < R; ++r )
			for ( int c = 0; c < C; ++c )
				cin >> m[ r ][ c ];
		int r = solve( R, C, m );
		cout << "Case #" << tc << ": ";
		if ( r == -1 )
			cout << "IMPOSSIBLE";
		else
			cout << r;
		cout << endl;
	}
	return 0;
}
