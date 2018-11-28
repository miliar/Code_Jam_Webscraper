#include<cstdio>
#include<algorithm>
using namespace std;

bool out( int x, int m, int M )
{
	if( x > M )
		return true;
	if( x == 4 && m == 2 && M == 4 )
		return true;
	for( int i = 0; i < x; ++i )
		if( min( i+1, x-i ) > m || max( i+1, x-i ) > M )
			return true;
	if( ( x+1 ) / 2 > m || ( x+2 ) / 2 > M )
		return false;
	for( int i = 1; i <= x; ++i )
		if( x % i == 0 )
			if( min( i, x/i ) > m )
				return true;
	return false;
}

int main()
{
	int t, x, r, c;

	scanf( "%d", &t );
	for( int n = 1; n <= t; ++n )
	{
		scanf( "%d %d %d", &x, &r, &c );
		if( out( x, min( r, c ), max( r, c ) ) || r * c % x )
			printf( "Case #%d: RICHARD\n", n );
		else
			printf( "Case #%d: GABRIEL\n", n );
	}
}
