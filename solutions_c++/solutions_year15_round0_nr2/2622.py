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

int n;
int p[maxn];

int main(){
//	freopen("B-small-attempt0.in", "r", stdin);
//	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int TT = 1; TT <= T; ++TT){
		scanf("%d", &n);
		int maxx = 0;
		for (int i = 0; i < n; ++i){
			scanf("%d", p + i);
			maxx = max(maxx, p[i]);
		}
		int ans = maxx, rc;
		for (int i = 1; i <= maxx; ++i){
			rc = 0;
			for (int j = 0; j < n; ++j){
				if (p[j] <= i) continue;
				rc += (p[j] - 1) / i;
			}
			ans = min(ans, rc + i);
		}
		printf("Case #%d: %d\n", TT, ans);
	}
	return 0;
}