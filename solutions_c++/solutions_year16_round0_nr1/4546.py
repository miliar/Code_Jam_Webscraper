#include<stdio.h>

FILE *in = fopen("input.txt", "r");
FILE *out = fopen("output.txt", "w");

int T;
int N;
int M;


int main()
{
	fscanf(in,"%d", &T);
	for (int t = 1; t <= T;t++)
	{
		int cnt[10] = { 0, };
		int cnt2 = 0;
		fscanf(in,"%d", &N);
		if (N == 0) {
			fprintf(out,"Case #%d: INSOMNIA\n",t);
		}
		else
		{
			for (int i = 1;; i++)
			{
				M = i*N;
				while (M != 0)
				{
					if (cnt[M % 10] == 0)
					{
						cnt2++;
						cnt[M % 10] = 1;
					}
					M /= 10;
				}
				if (cnt2 == 10)
				{
					fprintf(out,"Case #%d: %d\n", t,i*N);
					break;
				}

			}
		}
	}

}