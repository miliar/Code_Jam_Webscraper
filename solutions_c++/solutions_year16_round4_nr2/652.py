#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cmath>
#include <algorithm>
#include <assert.h>
#include <memory.h>
#include <string.h>
#include <complex>
#include <queue>
#include <cstdlib>
#include <ctime>
using namespace std;

#define ll long long
#define pb push_back
#define mp make_pair
#define sz(x) (int)(x).size()

double mas[222];

double dp[222][222];

double solve(vector<double> ver) {
	int N = sz(ver);
	for(int i = 0; i <= N; i++) 
		for(int j = 0; j <= N; j++) 
			dp[i][j] = 0.0;
	dp[0][0] = 1.0;
	for(int i = 0; i < N; i++) {
		for(int j = 0; j <= i; j++) {
			dp[i+1][j+1] += dp[i][j] * ver[i];
			dp[i+1][j] += dp[i][j] * (1.0-ver[i]);
		}
	}
	return dp[N][N/2];
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	int T;
	scanf("%d", &T);
	for(int test = 1; test <= T; test++) {
		printf("Case #%d: ", test);
		int N, K;
		scanf("%d %d", &N, &K);
		for(int i = 0; i < N; i++) cin >> mas[i];
		double res = 0.0;
		for(int mask = 0; mask < (1 << N); mask++) {
			int cnt = 0;
			for(int j = 0; j < N; j++) cnt += !!(mask & (1 << j));
			if(cnt != K) continue;
			vector<double> ver;
			for(int j = 0; j < N; j++) {
				if(mask & (1 << j)) ver.pb(mas[j]);
			}
			res = max(res, solve(ver));
		}
		printf("%.9lf\n", res);
	}

	return 0;
}