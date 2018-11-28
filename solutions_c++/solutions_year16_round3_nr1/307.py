#include <stdio.h>


int main()
{
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		int N;
		scanf("%d", &N);
		int P[26], Q[26];
		for (int i=0; i<N; i++) {
			scanf("%d", &P[i]);
			Q[i] = i;
		}
		for (int i=0; i<N; i++) {
			for (int j=i+1; j<N; j++) {
				if (P[i] < P[j]) {
					int tmp = P[i];
					P[i] = P[j];
					P[j] = tmp;
					tmp = Q[i];
					Q[i] = Q[j];
					Q[j] = tmp;
				}
			}
		}
		printf("Case #%d:", t);
		for (int i=P[1]; i<P[0]; i++) {
			printf(" %c", 'A' + Q[0]);
		}
		for (int i=2; i<N; i++) {
			for (int j=0; j<P[i]; j++) {
				printf(" %c", 'A' + Q[i]);
			}
		}
		for (int i=0; i<P[1]; i++) {
			printf(" %c%c", 'A' + Q[0], 'A' + Q[1]);
		}
		printf("\n");
	}
	return 0;
}
