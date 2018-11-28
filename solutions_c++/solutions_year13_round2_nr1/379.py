#include<stdio.h>
#include<iostream>
#include<queue>
#include<algorithm>
using namespace std;
__int64 b[1000005];
int main() {
	int t, cas = 0;
	__int64 a;
	int i, n, ans, p;
	scanf("%d", &t);
	while (t--) {
		cas++;
		scanf("%I64d%d", &a, &n);
		ans = n;
		for (i = 0; i < n; ++i)
			scanf("%I64d", &b[i]);
		sort(b, b + n);
		p = 0;
		for (i = 0; i < n; ++i) {
			if (a == 1)
				break;
			while (a <= b[i]) {
				p++;
				a = 2LL * a - 1;
			}
			a += b[i];
			//			printf("%d\n", p);
			ans = min(ans, p + n - i - 1);
		}
		printf("Case #%d: %d\n", cas, ans);
	}
}
