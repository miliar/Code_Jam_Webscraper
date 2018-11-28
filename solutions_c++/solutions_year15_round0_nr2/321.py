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

int a[1024], dp[1024][1024], n;

int main()
{
	for( int j = 1 ; j < 1024 ; j ++ )
		for( int i = 0 ; i < 1024 ; i ++ )
			if( i > j )
			{
				dp[i][j] = i;
				for( int k = 0 ; k <= i-k ; k ++ )
					dp[i][j] = min( dp[i][j], 1 + dp[k][j] + dp[i-k][j] );
			}
	int t, cc = 0;
	cin >> t;
	while( t -- )
	{
		cin >> n;
		for( int i = 0 ; i < n ; i ++ )
			cin >> a[i];
		int ans = 1024;
		for( int i = 1 ; i < 1024 ; i ++ )
		{
			int cur = 0;
			for( int j = 0 ; j < n ; j ++ )
				cur += dp[ a[j] ][i];
			ans = min( ans , cur + i );
		}
		cout << "Case #" << ++ cc << ": " << ans << endl;
	}
	return 0;
}
