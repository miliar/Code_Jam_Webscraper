#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <map>
#include <string>
#include <set>
#include <vector>
#include <queue>
#include <stack>
#include <bitset>
using namespace std;

typedef long long ll;
#define pb push_back

int next_permu( int p ) { 
	int x = (p&-p), y = p + x ; 
	return y | ( ( p & ~y ) / x >> 1 ) ; 
}

int n, k;
double ans, M;
double a[300];
vector<double>ta;
double dp[300][300];

double cal(){
	memset(dp, 0 ,sizeof(dp));
	dp[0][1] = ta[0];
	dp[0][0] = 1-ta[0];
	for(int i = 1; i < k; ++i)
		for(int j = 0; j < k; ++j){
			dp[i][j+1] += dp[i-1][j] * ta[i];
			dp[i][j] += dp[i-1][j] * (1-ta[i]) ;
		}
	return dp[k-1][k/2];
}

int main () {
	int t;
	scanf("%d", &t);
	for(int tt = 1; tt <= t; tt++){
		cin >> n >> k;
		ans = 0;
		for(int i = 0; i < n; ++i) cin >> a[i];
		int lower = (1<<k)-1, upper = 1 << n ; 
		for ( int comb = lower ; comb < upper ; ) {
			ta.clear();
			for(int i = 0; i < n; ++i) if(comb&(1<<i)) ta.pb(a[i]);
			double tmp = cal();
			ans = max(ans, tmp);
			comb = next_permu( comb ) ; 
		}
		printf("Case #%d: %.9f\n", tt, ans);
	}
}
