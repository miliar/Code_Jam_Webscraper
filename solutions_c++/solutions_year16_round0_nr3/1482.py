#include <cstdio>

typedef long long lint;

lint divider[20];

bool process(lint n, lint base) {
	lint val = 0;
	lint pow = 1;
	
	for (int i = 0; i <= 16; i++) {
		if ( n & (1LL<<i) ) {
			val += pow;
		}
		pow *= base;
	}

	//printf("%I64d na base %I64d = %I64d\n", n, base, val);
	
	for (lint k = 2; k * k < val; k++) {
		if (val % k == 0) {
			divider[base] = k;
			
			return true;
		}
	}
	
	return false;
}

void print_base2(lint n) {
	for (int i = 15; i >= 0; i--) {
		if ( n & (1LL<<i) ) {
			putchar('1');
		} else {
			putchar('0');
		}
	}
}

int main() {
	lint bot = 1LL<<15;
	lint top = (1LL<<16) + 1;
	
	int cnt = 0;
	bool work = false;
	
	printf("Case #1:\n");
	
	for (lint i = bot + 1; i < top; i += 2) {
		work = true;
		for (int base = 2; base <= 10; base++) {
			if (!process(i, base)) {
				work = false;
				break;
			}
		}
		
		if (work) {
			cnt++;
			print_base2(i);
			for (int base = 2; base <= 10; base++) {
				printf(" %I64d", divider[base]);
			}
			printf("\n");
		}
		
		if (cnt == 50) {
			break;
		}
	}
	
	return 0;
}