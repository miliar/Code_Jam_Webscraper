#include<cstdio>
#include<algorithm>
using namespace std;

int main()
{
	int t, size;

	scanf( "%d", &t );
	for( int n = 1; n <= t; ++n )
	{
		int shy[ 1001 ] = { 0 }, has = 0, ask = 0;

		scanf( "%d", &size );
		for( int i = 0; i <= size; ++i )
			scanf( "%1d", shy+i );
		for( int i = 0; i <= size; ++i )
			if( has >= i )
				has += shy[ i ];
			else
			{
				ask += i - has;
				has = i + shy[ i ];
			}
		printf( "Case #%d: %d\n", n, ask );
	}
}
