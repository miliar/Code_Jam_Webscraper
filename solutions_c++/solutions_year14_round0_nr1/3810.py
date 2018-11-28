//============================================================================
// Name        : Google.cpp
// Author      : Anmol Ahuja
//============================================================================

#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctype.h>
#include <cstdlib>
#include <climits>
#include <algorithm>
#include <iostream>
using namespace std;

inline void input( int ar[4][4] )
{
	int i,j;
	for( i=0; i<4; ++i )
	{
		for( j=0; j<4; ++j )
		{
			scanf( "%d", &ar[i][j] );
		}
	}
}

int main()
{
	int t;
	scanf("%d",&t);
	int ar1[4][4],ar2[4][4],ans1,ans2;
	for( int z=1; z<=t; ++z )
	{
		// row
		scanf( "%d", &ans1 );
		input(ar1);
		// cols
		scanf( "%d", &ans2 );
		input(ar2);

		bool flag = false;
		int sel;
		--ans1;--ans2;
		printf( "Case #%d: ", z );
		for( int i=0; i<4; ++i )
		{
			for( int j=0; j<4; ++j )
			{
				if( ar2[ans2][i] == ar1[ans1][j] )
				{
					if( flag )
					{
						printf( "Bad magician!" );
						goto out;
					}
					sel = ar2[ans2][i];
					flag = true;
				}
			}
		}
		if( !flag )
			printf( "Volunteer cheated!" );
		else
			printf( "%d", sel );
		out:
		printf( "\n" );
	}
	return 0;
}
