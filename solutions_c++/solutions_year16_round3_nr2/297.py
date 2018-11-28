#include <stdio.h>

int main()
{
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		int B;
		long long M;
		scanf("%d%lld", &B, &M);
		if (M > (1LL<<(B-2))) {
			printf("Case #%d: IMPOSSIBLE\n", t);
		} else if (M == (1LL<<(B-2))) {
			printf("Case #%d: POSSIBLE\n", t);
			for (int i=0; i<B; i++) {
				for (int j=0; j<B; j++) {
					printf("%d", j>i ? 1 : 0);
				}
				printf("\n");
			}
		} else {
			printf("Case #%d: POSSIBLE\n", t);
			for (int i=0; i<B; i++) {
				if (i==0) {
					for (int j=0; j<B; j++) {
						printf("%d", (M&(1LL<<(B-j-2))) ? 1 : 0);
					}
				} else {
					for (int j=0; j<B; j++) {
						printf("%d", j>i ? 1 : 0);
					}
				}
				printf("\n");
			}
		}
	}
	return 0;
}
/*
int main()
{
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		int B;
		int M;
		scanf("%d%d", &B, &M);
		int tri = 0;
		for (int i=0; i<B; i++) {
			tri += i;
		}
		bool f = false;
		for (unsigned int bit = 0; bit < (1U<<tri); bit++) {
			unsigned int b[6];
			unsigned int bit2 = bit;
			for (int i=0; i<B; i++) {
				int num = B-i-1;
				b[i] = bit2&((1<<num)-1);
				bit2 >>= num;
			}
			int p[6];
			p[0] = 1;
			for (int i=1; i<B; i++) {
				p[i] = 0;
				for (int j=0; j<i; j++) {
					if (b[j]&(1<<(B-i-1))) {
						p[i] += p[j];
					}
				}
			}
			if (p[B-1] == M) {
				printf("Case #%d: POSSIBLE\n", t);
				for (int i=0; i<B; i++) {
					for (int j=0; j<B; j++) {
						printf("%d", (b[i]>>(B-j-1))&1);
					}
					printf("\n");
				}
				f = true;
				break;
			}
		}
		if (!f) {
				printf("Case #%d: IMPOSSIBLE\n", t);
		}
	}
	return 0;
}
*/