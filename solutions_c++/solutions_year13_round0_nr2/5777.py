#include <stdio.h>

int main()
{
	FILE* fIn;
	FILE* fOut;
	fIn = fopen( "B-small-attempt0.in", "r" );
	fOut = fopen("Output.out", "w" );
	int Test_case;
	fscanf( fIn, "%d", &Test_case );
	for( int TC = 1 ; TC <= Test_case ; TC++ )
	{
		int lawn[100][100];
		int vertical, horizon;
		fscanf( fIn, "%d %d", &vertical, &horizon );
		for( int i = 0 ; i < vertical ; i++ )
		{
			for( int j = 0 ; j < horizon ; j++ )
			{
				fscanf( fIn, "%d", &lawn[i][j] );
			}
		}
		bool check_v = true;
		bool check_h = true;
		bool result = true;
		for( int i = 0 ; i < vertical ; i++ )
		{
			for( int j = 0 ; j < horizon ; j++ )
			{
				if( lawn[i][j] == 1 )
				{
					for( int k = 0 ; k < vertical ; k++ )
					{
						if( lawn[k][j] == 2 )
						{
							check_v = false;
							break;
						}
					}
					for( int k = 0 ; k < horizon ; k++ )
					{
						if( lawn[i][k] == 2 )
						{
							check_h = false;
							break;
						}
					}
				}
				if( check_v == false && check_h == false )
				{
					result = false;
				}
				else
				{
					check_v = true;
					check_h = true;
				}
			}
		}
		if( result == true )
		{
			fprintf( fOut, "Case #%d: YES\n", TC);
		}
		else
		{
			fprintf( fOut, "Case #%d: NO\n", TC);
		}
	}
	return 0;
}