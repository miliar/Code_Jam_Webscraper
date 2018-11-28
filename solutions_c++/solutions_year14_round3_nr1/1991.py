#include <iostream>
#include <stdio.h>

long long table[41] = {1};

int getIndex(long long q) {
	int j = 1;
	for (; j <= 40; j++) {
		if (q == table[j]) {
			return j;
		}
	}
	return -1;
}

int main() {
	int cases = 0;
	scanf("%d", &cases);
	
	for (int i = 1; i < 41; i++) {
		table[i] = table[i - 1] * 2;
	}
	for (int i = 1; i <= cases; i++) {
		long long p = 0;
		long long q = 0;
		scanf("%lld/%lld", &p, &q);
		
		if (getIndex(q) == -1) {
			long long extra = q % p;
			if (extra != 0) {
				printf("Case #%d: impossible\n", i);
				continue;
			}
			q = q / p;
			p = 1;
		}
		int k = 1;
		while(p * 2 < q) {
			k++;
			p *= 2;
		}
		printf("Case #%d: %d\n", i, k);
	}

	return 0;
}
