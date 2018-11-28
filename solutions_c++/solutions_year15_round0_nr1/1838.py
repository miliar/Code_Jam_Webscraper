#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;
char s[1010];
int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t = 0, tt;
	for (scanf("%d ", &tt); t < tt; ++t){
		int n;
		scanf("%d %s ", &n, s);
		int ans = 0;
		int cnt = 0;
		for (int i = 0; i <= n; ++i){
			ans = max(i - cnt, ans);
			cnt += s[i] - '0';
  		}
  		printf("Case #%d: %d\n", t + 1, ans);
	}
} 
