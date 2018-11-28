#include<stdio.h>
#include<string.h>
bool isp(__int64 a) {
	char s[100];
	int i, n;
	sprintf(s, "%I64d", a);
	n = strlen(s);
	for (i = 0; i < n; ++i) {
		if (s[i] != s[n - 1 - i])
			return false;
	}
	return true;
}
__int64 pp[100];
int main() {
	int T, cas = 0;
	int j, ans, ppn;
	__int64 i, a, b;
	ppn = 0;
	for (i = 1; i < 10000000; ++i) {
		if (isp(i) && isp(i * i)) {
			pp[ppn] = i * i;
			ppn++;
		}
	}
	scanf("%d", &T);
	while (T--) {
		cas++;
		ans = 0;
		scanf("%I64d%I64d", &a, &b);
		for (j = 0; j < ppn; ++j) {
			if (pp[j] >= a && pp[j] <= b)
				ans++;
		}
		printf("Case #%d: %d\n",cas, ans);
	}
}
