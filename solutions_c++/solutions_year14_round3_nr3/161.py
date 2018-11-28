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
#define INF 10000*100000
stringstream ss;
#define two(x) ( 1LL<<x )
#define sq(x) ( (x)*(x) )
LL mod = 1000000007LL;

/**************************Code****************************/

int mat[32][32];
int n, m, k;

int ok( int x , int y )
{
	int xx = x, yy = y;
	while( x >= 0 && !mat[x][y] )
		x --;
	if( x < 0 )
		return 0;
	x = xx;
	while( x < n && !mat[x][y] )
		x ++;
	if( x >= n )
		return 0;
	x = xx;
	while( y >= 0 && !mat[x][y] )
		y --;
	if( y < 0 )
		return 0;
	y = yy;
	while( y < m && !mat[x][y] )
		y ++;
	if( y >= m )
		return 0;
	return 1;
}

int can( int mask )
{
	int ans = 0, x = 0;
	memset( mat , 0 , sizeof mat );
	for( int i = 0 ; i < n ; i ++ )
		for( int j = 0 ; j < m ; j ++ )
			if( mask & two( i * m + j ) )
			{
				mat[i][j] = 1;
				ans ++;
			}
	for( int i = 0 ; i < n ; i ++ )
		for( int j = 0 ; j < m ; j ++ )
			if( !mat[i][j] )
				x += ok( i , j );
	if( ans + x < k )
		return 10000;
	return ans;
}

int main()
{
	int t, cc = 0;
	cin >> t;
	while( t -- )
	{
		cin >> n >> m >> k;
		int N = n * m, ans = 10000;
		for( int i = 0 ; i < two(N) ; i ++ )
			ans = min( ans , can( i ) );
		cout << "Case #" << ++ cc << ": " << ans << endl;
	}
	return 0;
}

