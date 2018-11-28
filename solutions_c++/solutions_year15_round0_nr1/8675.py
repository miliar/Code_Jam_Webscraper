#include <cstdio>
#include <iostream>
using namespace std;

int main () {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int tt = 1; tt <= t; tt++){
		int n;
		scanf("%d", &n);
		int a[1010];
		char s[1010];
		getchar();
		fgets(s, 1005, stdin);
		for(int i = 0; i <= n; i++) a[i] = s[i]-'0';
		int sum = a[0], ans = 0;
		for(int i = 1; i <= n; i++) {
			if(sum < i){
				ans += i - sum;
				sum = i;
			}
			sum += a[i];
		}
		printf("Case #%d: %d\n", tt, ans);
	}
}