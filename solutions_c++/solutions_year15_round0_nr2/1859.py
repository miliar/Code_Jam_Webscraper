#include <iostream>
#include <algorithm>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cmath>
using namespace std;

#define N 1000

int a[N+10], splitCnt[N+10][N+10];

void init(){
	for (int toBe = 1; toBe <= N; ++toBe){
		for (int i = toBe+1; i <=N; ++i){
			splitCnt[toBe][i] = INT_MAX;
			for (int j = 1; j <= i/2; ++j)
				splitCnt[toBe][i] =
					min(splitCnt[toBe][i], splitCnt[toBe][j] + splitCnt[toBe][i-j] + 1);
		}
	//	cerr<<"ToBe "<<toBe<<" processed"<<endl;
	}
}

int solve(){
	int n;
	scanf("%d", &n);
	int maxP = 0;
	for (int i = 0; i < n; ++i){
		scanf("%d", &a[i]);
		maxP = max(a[i], maxP);
	}
	
	int ans = INT_MAX;
	for (int toBe = 1; toBe <= maxP; ++toBe){
		
		int needSplit = 0;
		for (int i = 0; i < n; ++i)
			needSplit += splitCnt[toBe][a[i]];
			
		ans = min(ans, needSplit + toBe);
	}

	return ans;
}

int main(){
	init();
	int tests;
	scanf("%d", &tests);
	for (int test = 1; test <= tests; ++test)
		printf("Case #%d: %d\n", test, solve());

	return 0;
}
