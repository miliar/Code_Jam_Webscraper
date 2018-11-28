#include <stdio.h>

int T;
long long A, B;
int iA, iB;
long long target[1001];
int index;
long long reverse( long long );

int main()
{
	scanf( "%d", &T );
	for( int i = 0; i <= 1000; ++i )
		target[i] = 0;
	index = 0;
	for( long long i = 1; i <= 10000000; ++i )
	{
		if ( i == reverse( i ) && i*i == reverse( i*i ))
		{
			target[index] = i*i;
			++index;
		}
	}
	target[index] = 0x7fffffffffffffff;
	for( int p = 0; p < T; ++p )
	{
		scanf( "%lld %lld", &A, &B );
		for( int i = 0; i < 1001; ++i )
		{
			if( target[i] >= A )
			{
				iA = i;
				break;
			}
		}
		for( int i = 0; i < 1001; ++i )
		{
			if( target[i] > B )
			{
				iB = i;
				break;
			}
		}
		printf( "Case #%d: %d\n", p+1, iB - iA );
	}
	return 0;
}

long long reverse( long long _i )
{
	long long ans = 0;
	while( _i > 0 )
	{
		ans *= 10;
		ans += _i%10;
		_i /= 10;
	}
	return ans;
}