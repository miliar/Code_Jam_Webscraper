#include<stdio.h>

int N, M, T;
double A[16];
int BC[66666];

int main(void)
{
	int l0, l1, l2;
	int all, mult;

	BC[0] = 0;
	BC[1] = 1;
	for(l1 = 2; l1 < 66666; l1++)
	{
		BC[l1] = BC[l1 >> 1] + (l1 & 1);
	}

	scanf("%d", &T);
	for(l0 = 1; l0 <= T; l0++)
	{
		scanf("%d %d", &N, &M);
		for(l1 = 0; l1 < N; l1++) scanf("%lf", &A[l1]);

		double ret = 0;
		
		for(all = 0; all < (1 << N); all++)
		{
			if(BC[all] != M) continue;
			
			double curr = 0;
			for(mult = 0; mult < (1 << M); mult++)
			{
				if(BC[mult] == (M >> 1))
				{
					double term = 1;
					l1 = l2 = 0;
					for(l1 = 0; l1 < N; l1++) if(all & (1 << l1))
					{
						if(mult & (1 << l2))
						{
							term *= A[l1];
						}
						else
						{
							term *= (1 - A[l1]);
						}
						l2++;
					}
					curr += term;
//					printf("+%lf %d\n", term, mult);
				}
			}

			if(curr > ret)
			{
				ret = curr;
//				printf("%lf %d\n", ret, all);
			}
	
		}

		printf("Case #%d: %.12lf\n", l0, ret);
	}
	
	return 0;
}

