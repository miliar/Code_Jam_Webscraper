#include<bits/stdc++.h>

using namespace std;

double dp[20][20] , a[20];

double calc( int n ) {
	memset( dp , 0 , sizeof dp );
	dp[0][0] = 1;
	for( int i = 1 ; i <= n ; i++ ) {
		dp[i][0] = dp[i-1][0]*(1-a[i]);
		for( int j = 1 ; j <= i ; j++ )
			dp[i][j] = dp[i-1][j]*(1-a[i])+dp[i-1][j-1]*a[i];
	}
	return dp[n][n/2];
}

int main() {
	int t , n , k , len;
	double p[20];
	cin >> t;
	for( int ca = 1 ; ca <= t ; ca++ ) {
		double ans = 0;
		cin >> n >> k;
		for( int i = 0 ; i < n ; i++ )
			cin >> p[i];
		for( int i = 0 ; i < (1<<n) ; i++ ) {
			int tot = 0;
			for( int j = 0 ; j < n ; j++ )
				tot += (i>>j)&1;
			if( tot == k ) {
				len = 0;
				for( int j = 0 ; j < n ; j++ )
					if( (i>>j)&1 )
						a[++len] = p[j];
				ans = max( ans , calc( len ) );
			}
		}
		cout << "Case #" << ca << ": " << fixed << setprecision( 9 ) << ans << endl;
	}
	return 0;
}
