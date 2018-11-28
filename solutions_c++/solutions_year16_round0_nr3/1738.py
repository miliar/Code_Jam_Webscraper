#include <iostream>
#include <vector>
#include <array>
#include <algorithm>
#include <deque>

using namespace std;

long T = 0;
long N = 0;
long J = 0;

typedef unsigned int uint128_t __attribute__((mode(TI)));

vector< uint128_t > primes;

ostream& operator<<( ostream& os, uint128_t n )
{
	deque<char> s;
	while( n )
	{
		char d = n % 10;
		n /= 10;
		s.push_front( d + '0' );
	}
	for( auto d : s )
		os << d;
	return os;
}

void mersen( vector< uint128_t >& v, uint128_t max )
{
	uint128_t n = 2;
	while( n <= max )
	{
		bool isPrime = true;
		for( auto p : v )
			if (n % p == 0)
			{
				isPrime = false;
				break;
			}
		if(isPrime)
			v.push_back(n);
		n++;
	}
}

/**  jam candidate is 1 cbits 1 */
uint128_t toBase( uint128_t c, int b )
{
	uint128_t n = 0;
	uint128_t exp = 1;

	n += 1;
	exp *= b;

	for( int i = 0; i<N-2; i++ )
	{
		n += (c & 1) * exp;
		exp *= b;
		c>>= 1;
	}
	n += exp;
	return n;
}

uint128_t getDivider( uint128_t n )
{
	for( auto p : primes )
	{
		if( n % p == 0 )
			return p;
	}
	return 0;
}

bool isJamCoin( uint128_t c, array<uint128_t,9>& proof )
{
	for( int b = 2; b <= 10; ++b )
	{
		uint128_t n =  toBase( c, b );
		uint128_t d = getDivider( n );
		if( d == 0 )
			return false;
		proof[ b-2 ] = d;
	}
	return true;
}

int main(int argc, char * argv[] )
{
	
	cin >> T >> N >> J;

	uint128_t c=0; // count
	size_t j=0; // found

	mersen( primes, 1 << (N / 2) );

	cout << "Case #1:" << endl;
	while( j < J )
	{
		array<uint128_t,9> proof = {0,0,0,0,0,0,0,0,0};
		if( isJamCoin(c, proof) )
		{
			cout << toBase( c, 10 ) << ' ';
			for( auto p : proof )
				cout << p << ' ';
			cout << endl;
			++j;
		}
		++c;
	}
	return 0;
}