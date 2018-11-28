#include<iostream>
#include<cstdio>
#include<cstring>
int vis[15], num;
void f(__int64 n) {
	while (n) {
		int q = n % 10;
		if (vis[q] == 0)
			num++;
		vis[q] = 1;
		n /= 10;
	}
}
int main() {
	__int64 n;
	int T;
	int cas = 1;
	scanf("%d", &T);
	while (T--) {
		num = 0;
		__int64 n0 = n;
		__int64 k = 1;
		printf("Case #%d: ", cas++);
		scanf("%I64d", &n);
		memset(vis, 0, sizeof(vis));
		while (num < 10 && k < 1e4) {
			n0 = n * k;
			f(n0);
			k++;
		}
		if (num < 10)
			printf("INSOMNIA\n");
		else
			printf("%I64d\n", n0);
	}
	return 0;
}
