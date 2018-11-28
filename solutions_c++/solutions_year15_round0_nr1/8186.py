#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>

#define MAXLEVEL 1024

int main()
{
	int icase = 0;
	int level[MAXLEVEL];
	int stand[MAXLEVEL];
	char aud[MAXLEVEL];

	FILE *pfin;
	FILE *pfout;

	// std::fstream file("A-small.out",std::ios_base::out|std::ios_base::binary);
	// file.clear();

	pfin = fopen("A-large.in", "r" );
	pfout = fopen("A-large.out", "w+" );
	fscanf( pfin, "%d", &icase );
	// while ( fscanf( pfin, "%d", &icase ) != EOF )
	{
		for ( int i = 0; i < icase; i++ )
		{
			int maxlvl;
			int res = 0;

			memset( level, 0, MAXLEVEL );
			memset( stand, 0, MAXLEVEL );

			fscanf( pfin, "%d %s", &maxlvl, aud );
			
			for ( int j = 0; j <= maxlvl; j ++ )
			{
				level[j] = aud[j] - '0';

				if ( j == 0 )
				{
					stand[0] = level[0];
				}
				else
				{
					if ( level[j] == 0 || stand[j-1] >= j )
					{
						stand[j] = stand[j-1] + level[j];
					}
					else
					{
						res = res + j - stand[j-1];
						stand[j] = j + level[j];
					}
				}
			}

			//if ( (i+1) == icase ) fprintf ( pfout, "Case #%d: %d", i + 1, res );
			 fprintf ( pfout, "Case #%d: %d\n", i + 1, res );
		}
	}
	fclose( pfin );
	fclose( pfout );

	return 0;
}