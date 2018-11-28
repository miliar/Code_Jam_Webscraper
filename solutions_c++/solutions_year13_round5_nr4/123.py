#include<stdio.h>

long double D[1<<20];
char C[1<<20];
char str[111];
int n;
int T;
int l0;
long double prob;
int ALL;

void Go(int flag)
{
//	printf("%d..\n", flag);
	if(C[flag] != l0)
	{
		D[flag] = 0;
		C[flag] = l0;
		if(flag == ALL)
		{
			D[flag] = 0;
			return;
		}

		int l1, l2, first, next, diff;

		for(first = 0; first < n; first++)
		{
			if((flag & (1 << first)) == 0)
			{
				break;
			}
		}

		for(l1 = 0; l1 < n; l1++)
		{
			for(l2 = l1; l2 < n; l2++)
			{
				if((flag & (1 << l2)) == 0)
				{
					break;
				}
			}
			if(l2 == n)
			{
				next = (flag | (1 << first));
				diff = n + first - l1;
			}
			else
			{
				next = (flag | (1 << l2));
				diff = l2 - l1;
			}
			Go(next);
			D[flag] += prob * ((long double)n - (long double)diff + D[next]);
		}
	}
}

int main(void)
{
	int l1, l2;

	scanf("%d", &T);
	for(l0 = 1; l0 <= T; l0++)
	{
		scanf("%s", str);
		int init = 0;
		n = 0;
		for(l1 = 0; str[l1]; l1++)
		{
			n++;
			if(str[l1] == 'X')
			{
				init += (1 << l1);
			}
		}

		prob = 1 / (long double)n;
		ALL = ((1 << n) - 1);

		Go(init);

		printf("Case #%d: %.20Lf\n", l0, D[init]);
	}
}
