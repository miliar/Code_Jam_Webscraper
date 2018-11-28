#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <ctime>
#include <deque>
#include <stack>
#include <map>
#include <set>

using namespace std;

#define INF 1000000000000000000ll
#define inf 1000000000
#define ll long long
#define ull unsigned ll
#define mp make_pair
#define pb push_back 
#define F first
#define S second

int t;
int n;
int a[1005];
int dp[1005];

int calc(int val){
    int res = 0;
	for(int i = 1;i <= n;++ i)
		res += dp[a[i]];
	return res + val;				
}

int main (){
//	freopen("in", "r", stdin);
//	freopen("out", "w", stdout);
	scanf("%d", &t);
	for(int test = 1;test <= t;++ test){
		scanf("%d\n", &n);
		for(int i = 1;i <= n;++ i)	
			scanf("%d", &a[i]);
		int mn = inf;
		for(int ii = 1;ii <= 10;++ ii){
			for(int j = 1;j <= ii;++ j)
				dp[j] = 0;
			for(int j = ii + 1;j <= 10;++ j){
			    dp[j] = inf;
				for(int A = 1;A < j;++ A){
					int B = j - A;
					dp[j] = min(dp[j], dp[A] + dp[B] + 1);				
				}	
			}
			mn = min(mn, calc(ii));
		}	
		printf("Case #%d: %d\n", test, mn);
	}
	return 0;
}       