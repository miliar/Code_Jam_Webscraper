#include<stdio.h>

int T, X, N, See[10], Flag, Cnt;

int main(void)
{
	int l0, l1;

	scanf("%d", &T);
	for(l0 = 1; l0 <= T; l0++)
	{
		scanf("%d", &N);
		if(N == 0)
		{
			printf("Case #%d: INSOMNIA\n", l0);
			continue;
		}

		Flag++;
		Cnt = 0;
		X = N;
		while(1)
		{
			for(l1 = X; l1; l1 /= 10)
			{
				if(See[l1 % 10] != Flag)
				{
					See[l1 % 10] = Flag;
					Cnt++;
				}
			}
			if(Cnt == 10) break;
			X += N;
		}
		printf("Case #%d: %d\n", l0, X);
	}
	return 0;
}
