#include<stdio.h>
#include<string.h>
#define swap(aa,bb) {cc=aa;aa=bb;bb=cc;}
char cc;

// R < P < S < R

char A[4444];
char Ret[4444];
int Log;
int N, R, P, S;
int RR, PP, SS;

void Make(char me, int level)
{
	if(level == 0) A[N++] = me;
	else
	{
		if(me == 'P')
		{
			Make('P', level - 1);
			Make('R', level - 1);
		}
		else if(me == 'R')
		{
			Make('R', level - 1);
			Make('S', level - 1);
		}
		else if(me == 'S')
		{
			Make('P', level - 1);
			Make('S', level - 1);
		}
	}
}

char XX[4] = {'P', 'R', 'S', 0};
int xx;

int main(void)
{
	int T;
	int l0, l1, l2, l3;

	scanf("%d", &T);
	for(l0 = 1; l0 <= T; l0++)
	{
		scanf("%d %d %d %d", &Log, &R, &P, &S);

		Ret[0] = 0;

		for(xx = 0; xx < 3; xx++)
		{
			N = 0;
			Make(XX[xx], Log);
			A[N] = 0;
			RR = PP = SS = 0;
			for(l1 = 0; l1 < N; l1++)
			{
				if(A[l1] == 'R') RR++;
				if(A[l1] == 'P') PP++;
				if(A[l1] == 'S') SS++;
			}
			if(R == RR && P == PP && S == SS)
			{
				for(l1 = 1; l1 < N; l1 <<= 1)
				{
					for(l2 = 0; l2 < N; l2 += l1+l1) // start
					{
						int flag = 0;

						for(l3 = 0; l3 < l1; l3++) // compare
						{
//							printf("(%d,%d)", l2+l3, l2+l1+l3);
							if(A[l2+l3] > A[l2+l1+l3])
							{
								flag = 1;
								break;
							}
							else if(A[l2+l3] < A[l2+l1+l3])
							{
								break;
							}
						}
						if(flag)
						{
							for(l3 = 0; l3 < l1; l3++)
							{
								swap(A[l2+l3], A[l2+l1+l3]);
							}
						}
//						printf("\n");
					}
//					printf("\n");
				}

				if(Ret[0] == 0 || strcmp(Ret, A) > 0)
				{
					strcpy(Ret, A);
				}
			}
		}
		if(Ret[0] == 0) strcpy(Ret, "IMPOSSIBLE");
		printf("Case #%d: %s\n", l0, Ret);
	}
}
