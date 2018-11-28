#include <stdio.h>
#include <math.h>

int T;
long long r, t;
long long k;
long double tr, tt, tk;

int main()
{
	scanf( "%d", &T );
	for( int p = 0; p < T; ++p )
	{
		scanf( "%lld %lld", &r, &t );
		tr = r; tt = t;
		tk = sqrt( (2*tr-1)*(2*tr-1)+8*tt ) - ( 2*r+3 );
		tk /= 4;
		k = (long long)tk;
		printf( "Caes #%d: %lld\n", p+1, k+1 );
	}
	return 0;
}