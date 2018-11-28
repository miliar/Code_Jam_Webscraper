#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<vector>
#include<queue>
#include<map>
#include<iostream>
#include<algorithm>
using namespace std;

typedef long long LL;

const int maxn = 1005;
const int mod = (int)1e9 + 7;

char lev[maxn];
int smax;

int main(){
//	freopen("A-small-attempt0.in", "r", stdin);
//	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int TT = 1; TT <= T; ++TT){
		scanf("%d%s", &smax, lev);
		int ans = 0, sum = 0;
		for (int i = 0; i<=smax; ++i){
			if (lev[i] == '0') continue;
			ans = max(ans, i - sum);
			sum += lev[i] - '0';
		}
		printf("Case #%d: %d\n", TT, ans);
	}
	return 0;
}