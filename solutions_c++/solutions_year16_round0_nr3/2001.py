//
// Created by metopa on 09.04.2016.
//
#define _GLIBCXX_USE_INT128

#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <limits>

typedef __int128_t i128_t;

using namespace std;

extern vector<i128_t> primes;

i128_t getDivisor( i128_t x ) {
	for ( i128_t d : primes ) {
		if ( d > x )
			break;
		if ( x % d == 0 )
			return d;

	}
	return 0;
}

i128_t convertToBase( const vector<bool>& rep, int base ) {
	i128_t num = 0;
	for ( bool b : rep ) {
		num *= base;
		num += b;
	}
	return num;
}

vector<bool> nextJamcoin( uint32_t num, size_t size ) {
	vector<bool> rep( size, false );
	rep[0] = true;
	rep[size - 1] = true;
	for ( size_t i = size - 2; i > 0 && num > 0; --i, num /= 2 )
		rep[i] = num & 1;
	return rep;
}


ostream& operator <<( ostream& out, i128_t x ) {
	if ( x == 0 )
		return out << 0;
	if ( x < numeric_limits<int64_t>::max() )
		return out << (int64_t) x;
	out << x / 10;
	return out << (int) ( x % 10 );
}

int main() {
	size_t n = 0;
	size_t j = 0;
	size_t count = 0;
	uint32_t id = 0;
	ifstream in( "D:\\Sources\\C++\\CodeJam\\2016\\round_0\\in.txt" );
	ofstream out( "D:\\Sources\\C++\\CodeJam\\2016\\round_0\\out.txt" );

	vector<i128_t> divisors;
	divisors.reserve( 9 );

	out << "Case #1:" << endl;
	in >> n >> n >> j;
	while ( count < j ) {
		auto candidate = nextJamcoin( id++, n );
		if ( id == 0 )
			break;
		divisors.clear();
		bool success = true;
		for ( int i = 2; i <= 10 && success; i++ ) {
			divisors.push_back( getDivisor( convertToBase( candidate, i ) ) );
			success = (bool) divisors.back();
		}
		if ( success ) {
			for ( bool b : candidate )
				out << b ? '1' : '0';
			for ( i128_t d : divisors )
				out << ' ' << d;
			out << endl;
			count++;
		}
	}
	return 0;
}


vector<i128_t> primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
						 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173};
