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

char s[105];
bool v[1 << 16];
int p[1 << 16],c=0;
void pre(){
	int m = (1 << 16);
	for (int i = 2; i < m; i++) if(!v[i]){
		p[c++] = i;
		for (int j = i * 2; j < m; j += i){
			v[j] = 1;
		}
	}
}
int a[20];
int n, J;
bool judge(){
	for (int i = 2; i <= 10; i++){
		LL val = 0;
		for (int j = n-1; j >= 0; j--){
			val = val * i + a[j];
		}
		if (val < (1 << 16)){
			if (!v[val]) return 0;
		}
		else {
			bool ok = 0;
			for (int k = 0; k < c && p[k] * 1LL * p[k] <= val; k++){
				if(val % p[k] == 0) ok = 1;
			}
			if (!ok) return 0;
		}
	}
	return 1;
}
void dfs(int i){
	if (J <= 0) return;
	if (i == -1){
		if (judge()){
			for (int i = n-1; i >= 0; i--){
				printf("%d", a[i]);
			}
			printf(" ");
			for (int i = 2; i <= 10; i++){
				LL val = 0;
				for (int j = n-1; j >= 0; j--){
					val = val * i + a[j];
				}
				for (int k = 0; k < c && p[k] * 1LL * p[k] <= val; k++){
					if (val % p[k] == 0){
						printf("%d", p[k]);
						if (i != 10) printf(" ");
						else printf("\n");
						break;
					}
				}
			}
			J--;
		}
		return;
	}
	a[i] = 1;
	dfs(i - 1);
	if (i != 0 && i != n-1){
		a[i] = 0;
		dfs(i - 1);
	}
}
int main(){
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	int t;
	scanf("%d", &t);
	while (t--){
		scanf("%d%d", &n, &J);
		pre();
		printf("Case #1:\n");
		dfs(15);
	}
	return 0;
}