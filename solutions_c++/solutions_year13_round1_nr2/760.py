/*************************************************************************
Author: zjut_polym
Created Time:   2013/4/27 8:44:13
File Name: codejam.cpp
************************************************************************/
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <climits>
#include <queue>
using namespace std;


//----------------------[ZJUT-polym for div2]-------------------------------------
#define ll long long
#define MOD 1000000007
#define PII pair<int, int>
#define ff first
#define ss second
#define sz(v) (int)v.size()
#define _mst(buf, val) memset(buf, val, sizeof(buf))
#define rep(i, l, r) for(i = (l); i <= (r); i++)
#define srep(i, l, r) for(i = (l); i >= (r); i--)
#define repi(it, c) for(typeof(c.begin())it = c.begin(); it != c.end(); it++)
#define inf 0x3f3f3f3f
#define N 100005
#define eps 1e-8
#define pi (2.0 * acos(0.0))
//--------------------------------------------------------------------------------
int dp[105][105], v[105];
int main() {
	int C, cas = 1, e, r, n;
	scanf("%d", &C);
	while(C--){
		scanf("%d%d%d", &e, &r, &n);
		for(int i = 1; i <= n; i++){
			scanf("%d", &v[i]);
		}		
		memset(dp, 0, sizeof(dp));
		for(int i = 1; i <= n; i++){
			for(int j = 0; j <= e - r; j++){
				dp[i][j+r] = dp[i-1][j];
			}
			for(int j = 1; j < r && e-j >= 0; j++)
				dp[i][e] = max(dp[i][e], dp[i-1][e-j]);
			for(int j = 0; j <= e; j++){
				for(int k = 1; j+k <= e; k++){
					dp[i][j] = max(dp[i][j], dp[i][j+k] + k * v[i]);
				}
			}
		}
		int ans = 0;
		for(int i = 0; i <= e; i++){
			ans = max(ans, dp[n][i]);
		}
		printf("Case #%d: %d\n", cas++, ans);
	}	
    return 0;
}

