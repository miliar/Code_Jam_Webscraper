#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#define maxn 1010
#define mod 1000000007
using namespace std;
int a[1100], b[maxn], righ[maxn], f[maxn][maxn];



void solve(){
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; ++i){
		scanf("%d", &a[i]);
		b[i] = a[i];
	}
	sort(&b[1], &b[n + 1]);
	map<int,int> mm;
	for(int i = 1; i <= n; ++i) mm[b[i]] = i;
	for(int i = 1; i <= n; ++i) a[i] = mm[a[i]];
	for(int i = 1; i <= n; ++i){
		righ[a[i]] = 0;
		for(int j = 1; j <= n; ++j)if(a[j] > a[i] && j > i) ++righ[a[i]];
	}
	for(int i = 0; i <= n; ++i)
		for(int j = 0; j <= i; ++j) f[i][j] = mod;
	f[0][0] = 0;
	for(int i = 0; i < n; ++i)
		for(int j = 0; j <= i; ++j){
			int tmpl = n - i - 1 - righ[i + 1], tmpr = righ[i + 1];
			f[i + 1][j + 1] = min(f[i + 1][j + 1], f[i][j] + tmpl);
			f[i + 1][j] = min(f[i + 1][j + 1], f[i][j] + tmpr);
		}
	int ans = mod;
	for(int i = 0; i <= n; ++i) ans = min(ans, f[n][i]);
	printf("%d\n", ans);
	
}

int main(){
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i){
		printf("Case #%d: ", i);
		solve();
	}
}