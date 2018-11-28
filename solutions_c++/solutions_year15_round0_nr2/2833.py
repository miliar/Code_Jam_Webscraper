#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <queue>
#include<string>
using namespace std;
#define maxn 210000
#define LL long long
#define mods 1000000007
int a[1005];
int main(){
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int t; scanf("%d", &t);
	int kase = 0;
	while (t--){
		int n; scanf("%d", &n);
		for (int i = 1; i <= n; i++){
			scanf("%d", &a[i]);
		}
		int ans = 1e9;
		for (int i = 1; i <= 1000; i++){
			int cnt = 0;
			for (int j = 1; j <= n; j++){
				cnt += (a[j] + i - 1) / i - 1;
			}
			ans = min(ans, cnt + i);
		}
		printf("Case #%d: %d\n", ++kase, ans);
	}
	return 0;
}