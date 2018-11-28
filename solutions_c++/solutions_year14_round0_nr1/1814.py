#include<cstdio>
#include<cstring>
using namespace std;
int a[4][4], b[4][4];
int main()
{
	int cas, c = 0;
	scanf( "%d", &cas );
	while ( cas-- )
	{
		int n1,n2;
		scanf( "%d", &n1 );
		for ( int i = 0; i < 4; i++ )
			for ( int j = 0; j < 4; j++ )
			scanf( "%d", &a[i][j] );
		scanf( "%d", &n2 );
		for ( int i = 0; i < 4; i++ )
			for ( int j = 0; j < 4; j++ )
			scanf( "%d", &b[i][j] );
		int x, t = 0;
		for ( int i = 0; i < 4; i++ )
			for ( int j = 0; j < 4; j++ )
			if ( a[n1-1][i] == b[n2-1][j] ) 
			{
				t++;
				if ( t == 1 ) 
					x = a[n1-1][i];
			}
		c++;
		printf( "Case #%d: ", c );
		if ( t == 0 ) puts("Volunteer cheated!");
		else if ( t > 1 ) puts("Bad magician!");
		else printf( "%d\n", x );
	}

}