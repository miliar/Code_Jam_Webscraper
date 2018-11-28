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

int n, m, k;
int d[4][2] = { {1,0},{0,1} };

int f( int mask )
{
	int ret = 0;
	for( int i = 0 ; i < n ; i ++ )
		for( int j = 0 ; j < m ; j ++ )
			if( mask & two( i*m+j ) )
				for( int l = 0 ; l < 2 ; l ++ )
				{
					int x = i + d[l][0], y = j + d[l][1];
					if( 0 <= x && x < n && 0 <= y && y < m && ( mask & two( x*m+y ) ) )
						ret ++;
				}
	return ret;
}

int main()
{
	int t, cc = 0;
	cin >> t;
	while( t -- )
	{
		cin >> n >> m >> k;
		int ans = n * m * n;
		for( int i = 0 ; i < two(n*m) ; i ++ )
			if( __builtin_popcount( i ) == k )
				ans = min( ans, f( i ) );
		cout << "Case #" << ++ cc << ": " << ans << endl;
	}
	return 0;
}
