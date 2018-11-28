#include <stdio.h>
#include <string.h>

int t, cas;

int ms;
char str[10000];

int solve() {
	int ret = 0, acc = 0;
	for (int lvl = 0; lvl <= ms; lvl++) {
		int num = str[lvl] - '0';
		acc += num;
		if (acc < lvl + 1) {
			ret += (lvl + 1 - acc);
			acc = lvl + 1;
		}
	}
	return ret;
}

int main() {
	scanf("%d", &t);
	for (cas = 1; cas <= t; cas++) {
		scanf("%d%s", &ms, str);
		int ret = solve();
		printf("Case #%d: %d\n", cas, ret);
	}
	return 0;
}
