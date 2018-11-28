#include <bits/stdc++.h>

int main(void) {
	int T; scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		int N; scanf("%d", &N);
		int bm = 0;
		int j = 1;
		
		if (N == 0) {
			printf("Case #%d: INSOMNIA\n", i);
			continue;
		}
		
		while (bm != ((1 << 10) -1)) {
			int num = N * j;
			while (num > 0) {
				int last = num % 10;
				bm |= (1 << last);
				num /= 10;
			}
			j++;
		}
		printf("Case #%d: %d\n", i, (j-1)*N);
	}

}
