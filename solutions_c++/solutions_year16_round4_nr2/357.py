#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cstdlib>
#include<cmath>
#include<cctype>
#include<ctime>
#include<algorithm>
#include<iomanip>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<cassert>
#include<bitset>

using namespace std;

int n, k;
double a[300], b[300];
double dp[300][300];
double cal(){
	dp[0][0] = 1 - a[0];
	dp[0][1] = a[0];
	for(int i = 1; i < k; ++i){
		dp[i][0] = dp[i - 1][0] * (1 - a[i]);
		for(int j = 1; j <= i; ++j){
			dp[i][j] = dp[i - 1][j] * (1 - a[i]) + dp[i - 1][j - 1] * a[i];
		}
		dp[i][i + 1] = dp[i - 1][i] * a[i];
	}
	return dp[k - 1][k / 2];
}

int main() {
	int TT;
	scanf("%d", &TT);
	for(int cc = 1; cc <= TT; cc++){
		scanf("%d%d", &n, &k);
		for(int i = 0; i < n; ++i){
			cin >> b[i];
		}
		sort(b, b +n);
		double ans = 0;
		for(int pre = 0; pre <= k; ++pre){
			for(int i = 0; i < pre; ++i) a[i] = b[i];
			for(int i = n - (k - pre); i < n; ++i){
				a[i + k - n] = b[i];
			}
			double tmp = cal();
			if(tmp > ans) ans = tmp;
		}
		printf("Case #%d: %.10f\n", cc, ans);
	}
	return 0;
}

