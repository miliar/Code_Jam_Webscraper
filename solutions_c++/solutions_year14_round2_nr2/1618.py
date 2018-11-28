#include <stdio.h>
#include <string.h>

int r[1010];

void gen(int A, int B)
{
	int i, j;

	memset(r, 0, sizeof(r));
	for (i = 0; i < A; i++) 
		for (j = 0; j < B; j++) 
			r[i&j]++;
}

int main()
{
	int i, T, t, A, B, K, s;

	scanf("%d", &T);

	for (t = 1; t <= T; t++) {
		scanf("%d%d%d", &A, &B, &K);
		gen(A, B);

		for (i = s = 0; i < K; i++)
			s += r[i];

		printf("Case #%d: %d\n", t, s);
	}
	return 0;
}

