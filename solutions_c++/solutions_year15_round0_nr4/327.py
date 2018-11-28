#include <bits/stdc++.h>
using namespace std;
 
typedef pair< int , int > pii;
typedef long long LL;
#define fr first
#define se second
#define EPS 1e-8
#define INF 10000*10000*10000LL
stringstream ss;
#define two(x) ( 1LL<<x )
LL mod = 1000000007LL;

/**************************Code****************************/

int X, n, m, full;
/*vector < int > all[8];
int d[4][2] = { {1,0},{-1,0},{0,1},{0,-1} };
int dp[1<<17];
int val[6][6] = { {0,1,2,3,4,5}
				, {6,7,8,9,10,22}
				, {11,12,13,14,22,22}
				, {15,16,17,22,22,22}
				, {18,19,22,22,22,22}
				, {20,22,22,22,22,22}
				};

void show( int mask )
{
	cout << __builtin_popcount( mask ) << endl;
	for( int i = 0 ; i < n ; i ++ )
	{
		for( int j = 0 ; j < m ; j ++ )
			if( mask & two( i * m + j ) )
				cout << 1;
			else
				cout << 0;
		cout << endl;
	}
}
int go( int mask )
{
	if( mask == full )
		return 1;
	if( dp[mask] != -1 )
		return dp[mask];
	show( mask );
	for( int i = 0 ; i < all[X].size() ; i ++ )
		if( !( mask & all[X][i] ) && ( all[X][i] & full ) == all[X][i] )
			if( go( mask | all[X][i] ) )
				return dp[mask] = 1;
	return dp[mask] = 0;
}
int dfs( int mask, int x, int y )
{
	if( !( mask & two( val[x][y] ) ) )
		return 0;
	mask ^= two( val[x][y] );
	int ret = 1;
	for( int i = 0 ; i < 4 ; i ++ )
	{
		int nx = x + d[i][0], ny = y + d[i][1];
		if( 0 <= nx && nx < n && 0 <= ny && ny < m && ( mask & two( val[nx][ny] ) ) )
			ret += dfs( mask, nx, ny );
	}
	return ret;
}*/

int main()
{
/*	n = m = 6;
	for( int i = 0 ; i < two(21) ; i ++ )
	{
		int x = __builtin_popcount( i );
		if( x > 6 )
			continue;
		if( dfs( i, 0, 0 ) == x )
			all[x].push_back( i );
	}*/
	int t, cc = 0;
	cin >> t;
	while( t -- )
	{
		cin >> X >> n >> m;
		if( n > m )
			swap( n, m );
		int ok = 0;
		if( ( n * m ) % X || X > 6 )
			ok = 1;
		else
		{
			if( X == 1 )
				ok = 0;
			else if( X == 2 )
				ok = 0;
			else if( X == 3 )
				ok = n == 1;
			else if( X == 4 )
			{
				if( n < 3 || m < 3 )
					ok = 1;
				else
					ok = 0;
			}
		}
		cout << "Case #" << ++ cc << ": " << ( ok ? "RICHARD" : "GABRIEL" ) << endl;
	}
	return 0;
}
