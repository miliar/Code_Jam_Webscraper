#include <stdio.h>

int main()
{
	int T;

	scanf("%d", &T);
	for(int t=1; t<=T; t++)
	{
		int A, B, K;
		int count = 0;

		scanf("%d %d %d", &A, &B, &K);

		for(int i=0; i<A; i++) {
			for(int j=0; j<B; j++) {
				if ((i & j) < K) count++;	
			}
		}

		printf("Case #%d: %d\n", t, count);
	}
	return 0;
}
