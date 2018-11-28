#include <iostream>
#include <string>
#include <string.h>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <stack>

#define LL long long 

using namespace std;
const int maxn = 205;
const int inf = 1e9+7;

int n, k;
double p[maxn];
double pp[maxn];

double dp[maxn][maxn]; // n yes
double gao(int n){
	dp[0][0] = 1.0;
	for(int i=1;i<=n;i++){
		for(int j=0;j<=i;j++){
			dp[i][j] = 0.0;
			if ( j>=1 )
				dp[i][j] += dp[i-1][j-1] * pp[i];
			dp[i][j] += dp[i-1][j] * (1.0 - pp[i]);
		}
	}
	return dp[n][n/2];
}

int main(){

    int T; scanf("%d", &T);
    for(int it=1;it<=T;it++){
    	printf("Case #%d: ",it);
    	scanf("%d%d", &n, &k);
    	for(int i=1;i<=n;i++) scanf("%lf", &p[i]);

    	sort(p+1, p+n+1);

    	double ans = 0.0;
    	for(int i=0;i<=k;i++){
    		int m = 0;
    		for(int j=1;j<=i;j++)
    			pp[++m] = p[j];
    		for(int j=1;j<=k-i;j++)
    			pp[++m] = p[n-j+1];

    		ans = max(ans, gao(k) );
    	}
    	printf("%lf\n", ans);
    }   

    return 0;
}

