#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<iostream>
#include<queue>
using namespace std;

int n, k,B[20];
double p[20],dp[(1<<17)][20];
int cnt(int x){
	int ret = 0;
	while (x){
		if (x & 1)ret++;
		x >>= 1;
	}
	return ret;
}
int main(){
	freopen("B.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	B[0] = 1;
	for (int i = 1; i < 20; i++)B[i] = B[i - 1] * 2;
	int t,ca=0;
	scanf("%d", &t);
	while (t--){
		scanf("%d%d", &n, &k);
		for (int i = 0; i < n; i++) scanf("%lf", &p[i]);
		dp[0][0] = 1;
		double ret = 0;
		for (int i = 1; i < (1 << n); i++){
			for (int j = 0; j < n; j++) if (i&B[j]){
				for (int k = 0; k <= 8; k++){
					dp[i][k] = dp[i - B[j]][k] * (1 - p[j]) + dp[i - B[j]][k - 1] * p[j];
				}
			}
			if (cnt(i) == k){
				ret = max(ret, dp[i][cnt(i) / 2]);
			}
		}
		printf("Case #%d: %.9lf\n", ++ca, ret);
	}
	return 0;
}