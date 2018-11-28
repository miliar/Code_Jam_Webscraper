#include <iostream>

using namespace std;

int main()
{
	freopen( "B-large.in", "rt", stdin );
	freopen( "output2.txt", "wt", stdout );

	int T = 0;
	scanf( "%d", &T );

	int lawn[110][110] = {0,};

	for( int i = 0; i < T; i++ )
	{
		int N = 0;
		int M = 0;

		scanf( "%d", &N );
		scanf( "%d", &M );

		for( int j = 0; j < N; j++ )
			for( int k = 0; k < M; k++ )
				scanf( "%d", &lawn[k][j] );

/*		for( int j = 0; j < N; j++ )
		{
			for( int k = 0; k < M; k++ ) printf( "%d ", lawn[k][j] );
			printf( "\n" );
		}*/

		bool b = true;

		for( int j = 0; j < N; j++ )
		{
			for( int k = 0; k < M; k++ )
			{
				int valid = 0;
				for( int l = 0; l < N; l++ )
				{
					if( lawn[k][l] > lawn[k][j] )
					{
						valid++;
						break;
					}
				}

				for( int l = 0; l < M; l++ )
				{
					if( lawn[l][j] > lawn[k][j] )
					{
						valid++;
						break;
					}
				}

				if( valid == 2 )
				{
					b = false;
					goto there;
				}
			}
		}
there:
		if( b == true ) printf( "Case #%d: YES\n", i+1 );
		else if( b == false ) printf( "Case #%d: NO\n", i+1 );
	}

	return 0;
}