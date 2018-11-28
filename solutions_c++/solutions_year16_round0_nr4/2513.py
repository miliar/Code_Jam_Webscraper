#include<iostream>
#include<cstdio>
#include<cstring>
#include<math.h>
using namespace std;

int main() {
	__int64 T;
	int cas = 1;
	__int64 k, c, s;
	scanf("%I64d", &T);
	while (T--) {
		printf("Case #%d: ", cas++);
		scanf("%I64d%I64d%I64d", &k, &c, &s);
		__int64 ans = 0, i, j;
		for (i = k, j = 1; j < c; j++, i = i * k) {
			ans += i;
		}
		printf("1");
		for (i = 2; i <= k; i++) {
			printf(" %I64d", i + ans * (i - 1));
		}
		printf("\n");
	}
	return 0;
}
