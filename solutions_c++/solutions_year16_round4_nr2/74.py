#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <limits.h>
#include <math.h>
#include <time.h>
#include <iostream>
#include <functional>
#include <numeric>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <vector>
#include <string>
#include <bitset>
#include <map>
#include <set>
using namespace std;
typedef long long lint;
typedef long double llf;
typedef pair<int, int> pi;

int n, k;
double a[222];

double f(int x, int p1, int p2){
	if(x == n){
		if(p1 == 0 && p2 == 0) return 1;
		return 0;
	}
	if(p1 < 0 || p2 < 0) return 0;
	double ret1 = f(x+1, p1 - 1, p2) * a[x];
	double ret2 = f(x+1, p1, p2 - 1) * (1 - a[x]);
	double ret3 = f(x+1, p1, p2);
	return max(ret1, max(ret2, ret3));
}

double dp[205][205];

double solve(vector<double> v){
	dp[0][0] = 1;
	for(int i=0; i<=k/2; i++){
		for(int j=0; j<=k/2; j++){
			if(i == 0 && j == 0){
				dp[i][j] = 1;
				continue;
			}
			dp[i][j] = 0;
			if(i > 0){
				dp[i][j] += dp[i-1][j] * v[i+j-1];
			}
			if(j > 0){
				dp[i][j] += dp[i][j-1] * (1 - v[i+j-1]);
			}
		}
	}
	return dp[k/2][k/2];
}

int main(){
	int t;
	cin >> t;
	for(int i=1; i<=t; i++){
		printf("Case #%d: ",i);
		cin >> n >> k;
		for(int j=0; j<n; j++){
			cin >> a[j];
		}
		sort(a, a+n);
		double ret = 0;
		for(int i=0; i<=k; i++){
			vector<double> v;
			for(int j=0; j<i; j++){
				v.push_back(a[j]);
			}
			for(int j=n-(k-i); j<n; j++){
				v.push_back(a[j]);
			}
			ret = max(ret, solve(v));
		}
		cout << ret << endl;
	}
}