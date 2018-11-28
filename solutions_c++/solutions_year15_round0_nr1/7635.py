#include <stdio.h>

int main(void)
{
	int t;
	int Smax;
	int Speo;
	int ten;
	int i, j, k;
	int Sarr[1001];
	int ValA;
	int Ssum;
	char buf;
	FILE *in, *out;

	in = fopen("A-large.in", "r");
	out = fopen("A-large.out", "w");

	fscanf(in, "%d", &t);
	//scanf("%d", &t);

	for (i = 0; i < t; i++)
	{
		fscanf(in, "%d ", &Smax);
		//scanf("%d", &Smax);
		
		Ssum = 0;
		ValA = 0;
		
		ten = 1;


		for (j = 0; j < Smax + 1; j++)
		{
			fscanf(in, "%c", &buf);
			//scanf("%d", &Speo);
			Sarr[j] = buf - '0';

		}
		fscanf(in, "%*c");
		
		for (j = 0; j < Smax + 1; j++)
		{
			Ssum = Ssum + Sarr[j];

			if (j != Smax)
			{
				if (Sarr[j] == 0 && (Ssum < j + 1))
				{
					ValA++;
					Ssum++;
				}
			}
		}

		fprintf(out, "Case #%d: %d\n", i + 1, ValA);
		//printf("Case #%d: %d\n", i + 1, ValA);
	}
	
	return 0;
}