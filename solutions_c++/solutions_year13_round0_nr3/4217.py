#include <stdio.h>
#include <string.h>
#include <math.h>

const int MAXN = 10000000;

int a[10000001];

bool isv(long long n) {
	char s[16];
	int len;
	sprintf(s, "%lld", n);
	len = strlen(s);
	len--;
	for (int i = 0; i < len; i++, len--) {
		if (s[i] != s[len]) return false;
	}
	return true;
}

int main() {
	for (int i = 1; i <= MAXN; i++) {
		a[i] = a[i - 1];
		if (isv(i) && isv(((long long)i) * i)) a[i]++;
	}
	int T;
	scanf("%d", &T);
	for (int re = 1; re <= T; re++) {
		long long A, B;
		scanf("%lld%lld", &A, &B);
		A = ceil(sqrt(A));
		B = floor(sqrt(B));
		printf("Case #%d: %d\n", re, a[B] - a[A - 1]);
	}
}
