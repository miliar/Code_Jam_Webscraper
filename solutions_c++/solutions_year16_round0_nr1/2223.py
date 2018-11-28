#include <iostream>
#include <cstdio>

int main() {
	int T, N;
	scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		scanf("%d", &N);
		if(N == 0) {
			printf("Case #%d: INSOMNIA\n", i + 1);
		} else {
			bool digit[10] = {false};
			int count = 0;
			int j = N;
			while (true) {
				int k = j;
				while(k > 0) {
					if(digit[k % 10] == false) {
						digit[k % 10] = true;
						count++;
					}
					k /= 10;
				}
				if (count == 10) {
					printf("Case #%d: %d\n", i + 1, j);
					break;
				}
				j += N;
			}
		}
	}
}