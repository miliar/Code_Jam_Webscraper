#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <assert.h>

int main()
{
	FILE *fin, *fout;
	if ( !( fin = fopen( "A-small-attempt0.in", "r" ) ) ) return -1;

	if ( !( fout = fopen( "res.txt", "w" ) ) ) return -1;

	int nCases;
	fscanf( fin, "%d", &nCases );
	for( int iCase = 0; iCase < nCases; iCase++ )
	{
		int ans1;
		if ( fscanf( fin, "%d", &ans1 ) != 1 ) return -1;
		int cards1[4][4];
		for( int i = 0; i < 16; i++ )
			if ( fscanf( fin, "%d", (int*)cards1 + i ) != 1 )
				return -1;

		int ans2;
		if ( fscanf( fin, "%d", &ans2 ) != 1 ) return -1;
		int cards2[4][4];
		for( int i = 0; i < 16; i++ )
			if ( fscanf( fin, "%d", (int*)cards2 + i ) != 1 )
				return -1;

		assert( ans1 >= 1 && ans1 <= 4 );
		assert( ans2 >= 1 && ans2 <= 4 );

		ans1--;
		ans2--;

		int nAns = 0;
		int resCard;
		for( int i = 0; i < 4; i++ )
			for( int j = 0; j < 4; j++ )
			{
				if ( cards1[ans1][i] == cards2[ans2][j] )
				{
					nAns++;
					resCard = cards1[ans1][i];
				}
			}

		fprintf( fout, "Case #%d: ", iCase + 1 );
		if ( nAns == 1 )
			fprintf( fout, "%d", resCard );
		else if ( nAns == 0 )
			fprintf( fout, "Volunteer cheated!" );
		else fprintf( fout, "Bad magician!" );
		fprintf( fout, "\n" );
	}

	fclose( fin );
	fclose( fout );
}
