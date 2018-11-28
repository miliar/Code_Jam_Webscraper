/*
 * main.cpp
 *
 *  Created on: 11 ???, 2015 ?.
 *      Author: Tigran
 */



#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <cassert>

using std::cin;
using std::cout;
using std::endl;

typedef char q_type;

const q_type q_1 = 1, q_i = 2, q_j = 3, q_k = 4;

q_type multiply( q_type a, q_type b )
{
	if ( a > 0 && b > 0 ) {
		switch ( a ) {
		case q_1:
			switch ( b ) {
			case q_1: return q_1;
			case q_i: return q_i;
			case q_j: return q_j;
			case q_k: return q_k;
			default: assert( false ); }
			break;
		case q_i:
			switch ( b ) {
			case q_1: return q_i;
			case q_i: return -q_1;
			case q_j: return q_k;
			case q_k: return -q_j;
			default: assert( false ); }
			break;
		case q_j:
			switch ( b ) {
			case q_1: return q_j;
			case q_i: return -q_k;
			case q_j: return -q_1;
			case q_k: return q_i;
			default: assert( false ); }
			break;
		case q_k:
			switch ( b ) {
			case q_1: return q_k;
			case q_i: return q_j;
			case q_j: return -q_i;
			case q_k: return -q_1;
			default: assert( false ); }
			break;
		default:
			assert( false );
		}
		return q_1;
	}
	else if ( a < 0 && b < 0 )
		return multiply( -a, -b );
	else
		return -multiply( abs( a ), abs( b ) );
}

q_type power( q_type a, long long p )
{
	assert( p > 0 );
	if ( p == 1 )
		return a;
	if ( p % 2 == 0 ) {
		q_type x = power( a, p/2 );
		return multiply( x, x );
	}
	else {
		q_type x = power( a, p/2 );
		x = multiply( x, x );
		return multiply( x, a );
	}
}

bool solve( const std::string& s, long long count )
{
	int n = (int)s.length();
	std::vector< q_type > x( n );
	for ( int i = 0; i < n; ++i ) {
		if ( s[ i ] == 'i' )
			x[ i ] = q_i;
		else if ( s[ i ] == 'j' )
			x[ i ] = q_j;
		else if ( s[ i ] == 'k' )
			x[ i ] = q_k;
		else
			assert( false );
	}
	q_type x_prod = x[ 0 ];
	for ( int i = 1; i < n; ++i )
		x_prod = multiply( x_prod, x[ i ] );
	q_type whole_prod = power( x_prod, count );
	if ( whole_prod != -q_1 )
		return false;

	long long i_pos = 0;
	{
		long long i_search_size = std::min( n * count, n * 10000LL + 5 );
		q_type i_value = q_1;
		for ( ; i_pos < i_search_size && i_value != q_i; ++i_pos ) {
			i_value = multiply( i_value, x[ i_pos % n ] );
		}
		if ( i_value != q_i )
			return false;
	}

	long long k_pos = n * count;
	{
		long long k_search_size = std::min( n * count, n * 10000LL + 5 );
		q_type k_value = q_1;
		for ( ; k_pos + k_search_size > n * count && k_value != q_k; ) {
			--k_pos;
			k_value = multiply( x[ k_pos % n ], k_value );
		}
		if ( k_value != q_k )
			return false;
	}

	return i_pos < k_pos;
}

int main()
{
	int TC;
	cin >> TC;
	for ( int tc = 1; tc <= TC; ++tc ) {
		long long L, X;
		cin >> L >> X;
		std::string s;
		cin >> s;
		assert( (int)s.length() == L );
		cout << "Case #" << tc << ": " <<
				(solve( s, X ) ? "YES" : "NO") << endl;
	}
	return 0;
}
