#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;
int vis[10], num;
ll n;

void solve(ll x) {
	while(x) {
		int k = x % 10;
		x /= 10;
		if(!vis[k]) {
			num ++;
			vis[k] = 1;
		}
	}
}

int main(void) {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	while(t --) {
		scanf("%I64d", &n);
		static int ti = 0;
		printf("Case #%d: ", ++ ti);
		if(n == 0) {
			puts("INSOMNIA");
			continue;
		}
		memset(vis, 0, sizeof vis);
		num = 0;
		int i = 1;
		while(num < 10) {
			solve(n * i);
			i ++;
		}
		printf("%I64d\n", n * (i - 1));
	}
	return 0;
}

