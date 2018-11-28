#include <stdio.h>

bool chk[10];

bool confirm(void) {

	for (int i = 0; i < 10; i++) {
		if (chk[i] == false) return false;
	}
	return true;
}

void func(long long num) {

	long long temp = num;

	while (temp > 0) {
		chk[temp % 10] = true;
		temp /= 10;
	}
}

int main() {

	int T;
	scanf("%d", &T);

	for (int tt = 1; tt <= T; tt++) {

		long long num;
		scanf("%lld", &num);

		if (num == 0) {
			printf("Case #%d: INSOMNIA\n", tt);
			continue;
		}

		for (int i = 0; i < 10; i++) chk[i] = false;

		long long mul = 1;

		while (1) {

			func(num*mul);
			if (confirm()) {
				printf("Case #%d: %lld\n", tt, num*mul);
				break;
			}
			mul++;
		}
	}
}