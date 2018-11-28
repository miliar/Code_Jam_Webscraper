#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	int T;
	cin >> T;

	for( int test = 1; test <= T; test++ )
	{
		int N, M;
		int lawn[100][100];
		int maxInRow[100];
		int maxInColumn[100];
		memset( lawn, 0, sizeof lawn );
		memset( maxInRow, 0, sizeof maxInRow );
		memset( maxInColumn, 0, sizeof maxInColumn );

		cin >> N >> M;

		// read the data.
		for( int n=0; n<N; n++ )
		{
			for( int m=0; m<M; m++ )
			{
				cin >> lawn[n][m];
				if( lawn[n][m] > maxInRow[n] )
					maxInRow[n] = lawn[n][m];
				if( lawn[n][m] > maxInColumn[m] )
					maxInColumn[m] = lawn[n][m];
			}
		}

		// iterate and check.
		bool result = true;
		for( int n=0; n<N; n++ )
		{
			for( int m=0; m<M; m++ )
			{
				if( lawn[n][m] != maxInRow[n] && lawn[n][m] != maxInColumn[m] )
				{
					result = false;
					break;
				}
			}
			if( !result ) break;
		}
		
		cout << "Case #" << test << ": " << ( ( result ) ? "YES" : "NO" );
		cout << endl;
	}

	return 0;
}