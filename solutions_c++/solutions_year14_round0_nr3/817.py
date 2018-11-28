#include <bits/stdc++.h>
using namespace std;

const int TAM = 50;
const int BASE = 200;

int h, w;
int dp[TAM+1][TAM+1][TAM*TAM+3];

bool can ( int row, int col, int left )
{
	if ( left < 0 ) return 0;

	int& r = dp[row][col][left];
	if ( r != -1 ) return r;

	if ( col == w )
		return ( r = ( left == 0 ? 1 : 0 ) );

	if ( row == 1 && col != 0 && h != 1 )
		return ( r = ( can ( row-1, col, left ) ? 4 : 0 ) );

	if ( !( row == 1 && col+1 != w && col != 0 && h != 1 ) )
		if ( can ( row, col+1, left-row ) )
			return ( r = 3 );

	if ( !( col == 1 && row > 1 ) )
		if ( row != 0 && can ( row-1, col, left ) )
			return ( r = 2 );

	return ( r = 0 );

}

char mat[TAM+2][TAM+2];

void build ( int row, int col, int left )
{
	if ( col == w ) return;
	if ( row == 1 && col != 0 && h != 1 ) {
		build ( row-1, col, left );
		return;
	}

	int& r = dp[row][col][left];
	assert ( r );

	for ( int i = 0; i < h; ++i )
		mat[i][col] = ( i < row ? '.' : '*' );

	if ( r == 2 ) build ( row-1, col, left );
	if ( r == 3 ) build ( row, col+1, left-row );
}

int main ( )
{
	cin.tie(0);
	ios_base::sync_with_stdio(0);

	int nTests;
	cin >> nTests;
	for ( int test = 1; test <= nTests; ++test )
	{
		int k;
		cin >> h >> w >> k;
		k = h*w-k;

		memset ( dp, -1, sizeof ( dp ) );

		cout << "Case #" << test << ":\n";

		if ( !can(h,0,k) ) cout << "Impossible\n";
		else {
			build(h,0,k);
			mat[0][0] = 'c';
			for ( int i = 0; i < h; ++i ) {
				for ( int j = 0; j < w; ++j )
					cout << mat[i][j];
				cout << '\n';
			}
		}
	}
	
	return 0;
}
