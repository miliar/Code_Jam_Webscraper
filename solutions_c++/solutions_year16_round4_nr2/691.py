#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <cmath>
#include <iostream>
#include <set>
#include <fstream>
#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;
#define FOR(i,s,e) for (int i=(s); i<(e); i++)
#define FOE(i,s,e) for (int i=(s); i<=(e); i++)
#define FOD(i,s,e) for (int i=(s); i>=(e); i--)
#define pb(x) push_back(x)
#define ppb() pop_back()
#define mp(x,y) make_pair(x,y)
#define LL long long
#define ULL unsigned long long
#define eps 1e-9
#define pi acos(-1.0)
LL max(LL a,LL b){if (a>b){return a;} else {return b;}}
LL min(LL a,LL b){if (a<b){return a;} else {return b;}}

int t;
int n, k;
double p[501];

double dp[201][201];

double res;

double v[6001];

double solve3(int a, int b){
	if (a == 0){
		if (!b) return 1.00; else return 0.00;
	}

	if (dp[a][b] < -(1e-6)){
		dp[a][b] = (b == 0? 0.00: solve3(a - 1, b - 1)) * v[a] + 
			solve3(a - 1, b) * (1.00 - v[a]);
	}

	return dp[a][b];
}

void calc(){
	FOE(i, 0, 200) FOE(j, 0, 200) dp[i][j] = -1.00;
	solve3(k, k / 2);
}

void solve(){
	cin >> n >> k;
	FOE(i, 1, n) cin >> p[i];
	sort(p + 1, p + n + 1);
	res = 0.00;
	FOE(i, 0, k){
		int h = 0;
		FOE(j, 1, i) v[++h] = p[j];
		int cnt = n;
		while (h != k){
			v[++h] = p[cnt]; cnt--;
		}
		calc();
//		printf("%d %.12lf\n", i, dp[k][k / 2]);
		if (dp[k][k / 2] > res) res = dp[k][k / 2];
	}

		//FOE(j, 0, 200) FOE(k, 0, 200) dp[i][j][k] = -1.000;
	//dp[0][0][0] = 1.00;
	printf("%.12lf\n", res);
}

int main(){
	scanf("%d", &t);
	int tc = 0;
	while (t--){
		tc++;
		printf("Case #%d: ", tc);
		solve();
	}
    return 0;
}
