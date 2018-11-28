#include<stdio.h>

int main() {
	int i, j,k, T, cnt;
	long long iN, N;
	bool digit[11];
	freopen("A-large.in","r",stdin);
	freopen("output.out", "w", stdout);
	scanf("%d", &T);
	for (i = 1; i <= T; i++) {
		scanf("%lld", &N);
		if (N == 0) {
			printf("Case #%d: INSOMNIA\n", i);
			continue;
		}
		for (j = 0; j < 10; j++) digit[j] = 0;
		
		k = 0;
		while (1) {
			k++;
			iN = k * N;
			while (iN) {
				digit[iN % 10] = 1;
				iN /= 10;
			}


			cnt = 0;
			for (j = 0; j < 10; j++) if (digit[j] == 1) cnt++;
			if (cnt == 10) break;
		}
		printf("Case #%d: %lld\n", i, k*N);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}