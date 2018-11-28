#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;
char s[1005];
int main() {
	int t, cas = 0;
	int n, i, j, k;
	scanf("%d", &t);
	while (t--) {
		cas++;
		scanf("%d", &n);
		scanf("%s", &s);
		k = 0;
		j = 0;
		for (i = 0; i <= n; ++i) {
			if (i > k) {
				j += i - k;
				k = i;
			}
			k += s[i] - '0';
		}
		printf("Case #%d: %d\n", cas, j);
	}
}
