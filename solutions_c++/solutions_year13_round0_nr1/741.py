#include <iostream>
#include <stdio.h>
#include <string>
#include <algorithm>
using namespace std;

#define valid(a)		(0<=(a)&&(a)<N)

const int N = 4;
const int NDIRS = 8;
const int dx[] = { -1,-1,-1, 0, 0, 1, 1, 1 };
const int dy[] = { -1, 0, 1,-1, 1,-1, 0, 1 };

const string O_WON = "O won";
const string X_WON = "X won";
const string DRAW = "Draw";
const string NOT_COMPLETED = "Game has not completed";

char mat[N][N+5];
int cnt[300];

int main ( )
{
	freopen ( "A.in", "r", stdin );
	freopen ( "A.out", "w", stdout );

	int nCases;
	scanf ( "%d", &nCases );
	for ( int curCase = 1; curCase <= nCases; ++curCase )
	{
		for ( int x = 0; x < N; ++x )
			scanf ( "%s", mat[x] );
		
		string ans = DRAW;
		for ( int x0 = 0; x0 < N; ++x0 )
			for ( int y0 = 0; y0 < N; ++y0 )
			{
				if ( ans == DRAW && mat[x0][y0] == '.' )
					ans = NOT_COMPLETED;

				for ( int d = 0; d < NDIRS; ++d )
				{
					if ( !valid ( x0 + (N-1)*dx[d] ) ) continue;
					if ( !valid ( y0 + (N-1)*dy[d] ) ) continue;
					cnt['O'] = cnt['X'] = cnt['T'] = 0;
					
					int x = x0, y = y0;
					for ( int i = 0; i < N; ++i )
					{
						cnt[(int)mat[x][y]]++;
						x+=dx[d], y+=dy[d];
					}

					if ( cnt['O'] + cnt['T'] == 4 && cnt['T'] <= 1 )
						ans = O_WON;
					
					if ( cnt['X'] + cnt['T'] == 4 && cnt['T'] <= 1 )
						ans = X_WON;
				}
			}
		
		printf ( "Case #%d: ", curCase );
		cout << ans << endl;
	}
	
	return 0;
}
