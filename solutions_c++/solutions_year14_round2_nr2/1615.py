#include <stdio.h>

int cases, kejs;
int i, j, A, B, K, k;

int main() {
    scanf("%d", &cases);
    for (kejs = 1; kejs <= cases; kejs++) {
        printf("Case #%d: ", kejs);
				scanf("%d%d%d", &A, &B, &K);
				for (k = i = 0; i < A; i++) {
					for (j = 0; j < B; j++) {
						if ((i&j) < K) k++; 
					}
				}
				printf("%d\n", k);
    }
    return 0;
}
