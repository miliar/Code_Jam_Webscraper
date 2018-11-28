#include<iostream>
#include<cstdio>
#include<cstring>
#include<math.h>
using namespace std;
__int64 mp[510];
bool f(__int64 n, __int64 k) {
	__int64 w = sqrt(n), i;
	for (i = 2; i <= w; i++) {
		if (n % i == 0)
			break;
	}
	if (i > w)
		return 1;
	return 0;
}
__int64 f0(__int64 n, __int64 k) {
	__int64 num;
	num = 0;
	while (n) {
		num = num * k + n % 2;
		n /= 2;
	}
	return num;
}
__int64 f1(__int64 n, __int64 k) {
	__int64 num;
	num = 0;
	while (n) {
		num = num * k + n % 2;
		n /= 2;
	}
	for (int i = 2;; i++) {
		if (num % i == 0)
			return i;
	}
}
int main() {
	int T;
	int n, j;
	__int64 i;
	scanf("%d", &T);
	while (T--) {
		printf("Case #1:\n");
		scanf("%d%d", &n, &j);
		__int64 p = (1 << (n - 1)) + 1, q = (1 << n) - 1;
		__int64 k;
		__int64 num = 0;
		for (i = p; i <= q && num < j; i += 2) {
			for (k = 2; k <= 10; k++) {
				__int64 r = f0(i, k);
				if (f(r, k))
					break;
			}
			if (k == 11)
				mp[num++] = i;
		}
		for (i = 0; i < num; i++) {
			__int64 e = mp[i], e0;
			e0 = e;
			while (e0) {
				printf("%d", e0 % 2);
				e0 /= 2;
			}
			for (k = 2; k <= 10; k++)
				printf(" %I64d", f1(e, k));
			printf("\n");
		}
	}
	return 0;
}
