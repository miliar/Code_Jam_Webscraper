#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <stdlib.h>
#include <sstream>
#include <assert.h>
#include <memory.h>
#include <string.h>
#include <time.h>
using namespace std;
#pragma comment(linker, "/STACK:100000000")

#define mp make_pair
#define pb push_back 
#define ll long long
#define sz(x) (int)(x).size()

int mas[1010];
int dp[1010][1010];


int get(int val, int low) {
	if(dp[val][low] == -1) {
		if(val <= low) return dp[val][low] = 0;
		int res = 1e9;
		for(int i = val - 1; i >= 1; i--) {
			res = min(res, get(i, low) + get(val - i, low) + 1);
		}
		return dp[val][low] = res;
	}
	return dp[val][low];
}

int main()
{
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	//freopen("onlyone.in","rt",stdin);
	//freopen("onlyone.out","wt",stdout);
	memset(dp, -1, sizeof(dp));
	int t;
	scanf("%d", &t);
	for(int test = 1; test <= t; test++) {
		int D;
		scanf("%d", &D);
		for(int i = 0; i < D; i++) scanf("%d", &mas[i]);
		int res = 1e9;
		for(int low = 1000; low > 0; low--) { // до куда понижаю
			int cnt = 0;
			for(int i = 0; i < D; i++) {
				cnt += get(mas[i], low);
			}
			res = min(res, low + cnt);
		}
		printf("Case #%d: %d\n", test, res);
	}

    return 0;
}