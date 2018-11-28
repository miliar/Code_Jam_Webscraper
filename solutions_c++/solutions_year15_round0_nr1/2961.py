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
int t;
int n;
int a[1500];
char s[1500];
int main(){
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &t);
	int kase = 0;
	while (t--){
		scanf("%d", &n);
		scanf("%s", &s);
		int cnt = 0;
		int ans = 0;
		for (int i = 0; i <= n; i++){
			if (s[i] != '0'){
				if (cnt < i){
					ans += i - cnt; cnt = i;
				}
				cnt += s[i] - '0';
			}
		}
		printf("Case #%d: %d\n", ++kase, ans);
	}
	return 0;
}