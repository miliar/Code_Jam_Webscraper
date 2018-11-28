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
 
#define For(i,n) for( int i=0; i < n; i++)
#define FOR(i,a,b) for( __typeof(b) i=(a); i<=(b); i++)
#define ALL(c)  c.begin() , c.end()
#define LL long long
#define int64 LL
#define Set(t,v) memset((t), (v), sizeof(t))

typedef vector < int > VI;
typedef pair< int , int > PII;
#define fr first
#define se second
#define pi M_PI
#define rad(x) (x)*acos(-1)/180.0
#define EPS 1e-6
#define INF 10000*10000
stringstream ss;
#define two(x) ( 1LL<<x )
#define sq(x) ( (x)*(x) )
LL mod = 1000000007LL;

/**************************Code****************************/

int mat[110][110], n, m;

int f( int x , int y )
{
	int r = 0, c = 0;
	for( int i = 0 ; i < n ; i ++ )
		r |= mat[i][y] > mat[x][y];
	for( int i = 0 ; i < m ; i ++ )
		c |= mat[x][i] > mat[x][y];
	return !r || !c;
}

int main()
{
	int t, cc = 0;
	cin >> t;
	while( t -- )
	{
		cin >> n >> m;
		int ok = 1;
		for( int i = 0 ; i < n ; i ++ )
			for( int j = 0 ; j < m ; j ++ )
				cin >> mat[i][j];
		for( int i = 0 ; i < n ; i ++ )
			for( int j = 0 ; j < m ; j ++ )
				ok &= f( i , j );
		cout << "Case #" << ++ cc << ": " << ( ok ? "YES" : "NO" ) << endl;
	}
	return 0;
}