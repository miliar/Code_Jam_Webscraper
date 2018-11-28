#include <stdio.h>
#include <string.h>

using namespace std;

typedef long long LL;

LL func(char* str, int base) {
	int len = strlen(str);
	LL res = 0;
	for (int i = 0; i < len; ++i) {
		res = 1LL * res * base + (str[i] - '0');
	}
	return res;
}
LL get_divisor(LL x) {
	for (LL i = 2; 1LL * i * i <= x; ++i) {
		if (x % i == 0) {
			return i;
		}
	}
	return 0;
}
int main() {
	freopen("C_output.txt", "w", stdout);
	char str[20];
	str[0] = str[15] = '1';
	str[16] = '\0';
	LL ans[15];
	LL count = 0;
	printf("Case #1:\n");
	for (int i = 0; count < 50 && i < (1 << 14); ++i) {
		for (int j = 0; j < 14; ++j) {
			if (i & (1 << j)) {
				str[j + 1] = '1';
			} else {
				str[j + 1] = '0';
			}
		}
		int tmp = 0;
		for (int j = 2; j <= 10; ++j) {
			LL val = func(str, j);
			LL div = get_divisor(val);
			if (div > 0) {
				ans[j] = div;
				++tmp;
			} else {
				break;
			}
		}
		if (tmp == 9) {
			++count;
			printf("%s", str);
			for (int j = 2; j <= 10; ++j) {
				printf(" %lld", ans[j]);
			}
			printf("\n");
		}
	}
	return 0;
}
