#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

void solve(int no) {
	int N = 0;
	scanf("%d", &N);
	printf("Case #%d: ", no);

	uint64_t x = N;
	char str[32];
	uint8_t table[10] = { 0 };
	uint8_t comp[10];
	memset(comp, 1, sizeof(comp));
	uint64_t ans = 0;
	for (uint64_t k = 1; k <= 1000000; k++) {
		uint64_t t = x * k;
		sprintf(str, "%llu", t);
		const char *p = str;
		while (*p != '\0') {
			table[*p - '0'] = 1;
			p++;
		}
		if (memcmp(table, comp, sizeof(table)) == 0) {
			ans = t;
			break;
		}
	}
	if (ans == 0) {
		puts("INSOMNIA");
	}
	else {
		printf("%llu\n", ans);
	}
}

int main() {
	int T = 0;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		solve(i);
	}
}
