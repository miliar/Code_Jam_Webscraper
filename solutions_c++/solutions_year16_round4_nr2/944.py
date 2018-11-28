#include <bits/stdc++.h>
using namespace std;

int T,K,N;
double dp[202][202];
double p[202];
int main(){
	scanf("%d",&T);
	for(int t=1; t<=T; t++){
		scanf("%d%d",&N,&K);
		for(int i=0; i<N; i++)
			scanf("%lf",&p[i]);
		
		double ans = 0.0;
		for(int i=0; i<1<<N; i++){
			vector<double> vv; vv.push_back(0.0);
			for(int j=0; j<N; j++){
				if( (1<<j)&i ) vv.push_back( p[j] );
			}
			if( vv.size() != K+1 ) continue;
			
			memset( dp, 0, sizeof dp );
			dp[0][0] = 1.0;
			for(int j=1; j<=K; j++){
				dp[j][0] = dp[j-1][0] * ( 1 - vv[j] );
				for(int k=1; k<=K/2; k++){
					dp[j][k] = dp[j-1][k] * ( 1 - vv[j] )
							  +dp[j-1][k-1] * ( vv[j] );
				}
			}
			ans = max( ans, dp[K][K/2] );
		}
		printf("Case #%d: %.10f\n", t, ans );
	}
	return 0;
}
