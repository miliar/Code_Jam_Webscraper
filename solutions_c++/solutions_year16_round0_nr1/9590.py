#include <stdio.h>
#include <stdlib.h>

int main() {
	int T;

	scanf("%d", &T);

	for(int i = 1; i <= T; i++) {
		unsigned long long n;
		scanf("%lld", &n);

		int index = 1, count = 0, check[10] = {0, };
		unsigned long long m = n;
		while(m > 0 && count < 10) {
			
			while(m > 0) {
				int t = m % 10;

				if(check[t] == 0) {
					check[t] = 1;
					count++;
				}

				m /= 10;
			}

			m = n * ++index;
		}

		if(count == 10) 
			printf("Case #%d: %lld\n", i, n*--index);
		else
			printf("Case #%d: INSOMNIA\n", i);
	}

	return 0;
}