#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <algorithm>
using namespace std;
double dp[205][205];

int n, k;
void update(double &a, double b){
	a += b;
}
double DP(vector<double>p){
	memset(dp,0,sizeof(dp));
	dp[1][1] = p[0];
	dp[1][0] = 1 - p[0];
	for(int i = 1; i < k; i++)
		for(int j=0;j<=k;j++){
			update(dp[i+1][j], dp[i][j] * (1-p[i]));
			update(dp[i+1][j+1], dp[i][j] * (p[i]));
		}
	return dp[k][k/2];
}

int main(){
	int T;
	cin >> T;
	double p[205];
	for(int _=1;_<=T;_++){
		cin >> n >> k;
		for(int i = 0;i<n;i++)
			cin >> p[i];
		sort(p, p +n);
		double ans = 0;
		for(int s = 0; s <= k; s++){
			vector<double>t;
			for(int i=0;i<s;i++)
				t.push_back(p[i]);
			int j = n - 1;
			while(t.size() < k){
				t.push_back(p[j]);
				j--;
			}
			double test = DP(t);
			if(test > ans)
				ans = test;
		}
		printf("Case #%d: %lf\n", _, ans);
		// cout << ans << endl;
	}
	return 0;
}