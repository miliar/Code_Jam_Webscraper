#include <stdio.h>
#include <iostream>
using namespace std;
char s[1005];
int main() {
	int t, cas = 0;
	int n, i, j, k;
	scanf("%d", &t);
	while (t--) {
		cas++;
		scanf("%d", &n);
		scanf("%s", s);
		int ans = 0;
		k = 0;
		for (i = 0; i <= n; ++i) {
			ans += max(0, i - k);
			k = max(k, i);
			k += s[i] - '0';
		}
		printf("Case #%d: %d\n", cas, ans);
	}
}

