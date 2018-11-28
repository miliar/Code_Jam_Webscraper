#include <list>
#include <set>
#include <map>
#include <ctime>
#include <stack>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <queue>
#include <deque>
#include <bitset>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <iterator>
#include <cassert>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <complex>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
 
#define LL long long
#define int64 LL

typedef vector < int > VI;
typedef pair< int , int > pii;
typedef pair < LL , LL > PLL;
#define fr first
#define se second
#define pi M_PI
#define rad(x) (x)*acos(-1)/180.0
#define EPS 1e-6
#define INF 10000*10000*10000LL
stringstream ss;
#define two(x) ( 1LL<<x )
#define sq(x) ( (x)*(x) )
LL mod = 1000000007LL;

/**************************Code****************************/

int r, c, mask;
int mark[32][32];
pii ans[6][6][36];
int ones[1<<25];
int d[8][2] = { {-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}, };

int val( int x , int y )
{
	if( mask & two(x*c+y) )
		return -1;
	int ret = 0;
	for( int i = 0 ; i < 8 ; i ++ )
	{
		int nx = x + d[i][0], ny = y + d[i][1];
		if( 0 <= nx && nx < r && 0 <= ny && ny < c && ( mask & two(nx*c+ny) ) )
			ret ++;
	}
	return ret;
}
int DFS( int x , int y )
{
	int ret = mark[x][y] = 1;
	if( val( x , y ) )
		return ret;
	for( int i = 0 ; i < 8 ; i ++ )
	{
		int nx = x + d[i][0], ny = y + d[i][1];
		if( 0 <= nx && nx < r && 0 <= ny && ny < c && !mark[nx][ny] )
			ret += DFS( nx , ny );
	}
	return ret;
}
int ok( int Mask , int R , int C , int st )
{
	r = R, c = C, mask = Mask;
	memset( mark , 0 , sizeof mark );
	if( DFS( st / c , st % c ) == r * c - ones[ mask ] )
		return 1;
	return 0;
}

int main()
{
	for( int i = 1 ; i < two(25) ; i ++ )
		ones[i] = ones[ i - ( i&(-i) ) ] + 1;
	for( int i = 0 ; i <= 5 ; i ++ )
		for( int j = 0 ; j <= 5 ; j ++ )
			for( int k = 0 ; k <= 30 ; k ++ )
				ans[i][j][k] = pii( -1 , -1 );
	int t, cc = 0;
	for( int R = 1 ; R <= 5 ; R ++ )
		for( int C = 1 ; C <= 5 ; C ++ )
			for( int i = 0 ; i < two(R*C) ; i ++ )
				if( ans[R][C][ ones[i] ].fr == -1 )
					for( int k = 0 ; k < R*C ; k ++ )
						if( !( i & two(k) ) )
							if( ok( i , R , C , k ) )
							{
								ans[R][C][ ones[i] ] = pii( i , k );
								break;
							}
	cin >> t;
	while( t -- )
	{
		int m;
		cin >> r >> c >> m;
		cout << "Case #" << ++ cc << ":" << endl;
		if( ans[r][c][m].fr == -1 )
			cout << "Impossible" << endl;
		else
		{
			for( int i = 0 ; i < r ; i ++ )
			{
				for( int j = 0 ; j < c ; j ++ )
					if( ans[r][c][m].fr & two(i*c+j) )
						cout << '*';
					else if( ans[r][c][m].se == i*c+j )
						cout << 'c';
					else
						cout << '.';
				cout << endl;
			}
		}
	}
	return 0;
}
