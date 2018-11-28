#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;
const int maxn = 1000005;
typedef long long LL;

int main(){
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	int t,k,c,s,ca=0;
	scanf("%d", &t);
	while (t--){
		scanf("%d%d%d", &k, &c, &s);
		printf("Case #%d: ", ++ca);
		for (int i = 1; i <= k; i++){
			printf("%d", i);
			if (i == k) printf("\n");
			else printf(" ");
		}
	}
	return 0;
}