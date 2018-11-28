#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;
const int maxn = 1000000;
typedef long long LL;
int a[maxn+5];
int st;
void get(int x){
	while (x){
		int u = x % 10;
		st |= (1 << u);
		x /= 10;
	}
}
int main(){

	for (int i = 1; i <= maxn; i++){
		st = 0;
		for (int j = i; st != 1023; j += i){
			get(j);
			a[i] = j;
		}
	}
	int n,t,ca=0;
	scanf("%d", &t);
	while (t--){
		scanf("%d", &n);
		if (!n) printf("Case #%d: INSOMNIA\n",++ca);
		else printf("Case #%d: %d\n", ++ca, a[n]);
	}
	return 0;
}