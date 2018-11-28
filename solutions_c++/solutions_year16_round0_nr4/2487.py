#include<stdio.h>

int T;
int K, C, S;

int main(void)
{
	int l0, l1;

	scanf("%d", &T);
	for(l0 = 1; l0 <= T; l0++)
	{
		scanf("%d %d %d", &K, &C, &S);
		printf("Case #%d:", l0);
		for(l1 = 1; l1 <= S; l1++) printf(" %d", l1);
		printf("\n");
	}
	return 0;
}
