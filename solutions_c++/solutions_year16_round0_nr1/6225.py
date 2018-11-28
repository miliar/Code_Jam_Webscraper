#include <stdio.h>
#include <string.h>

int main()
{
	FILE *infile, *outfile;
	infile = fopen("A-large.in", "r");
	outfile = fopen("A-output", "w");

	int t;
	fscanf(infile, "%d\n", &t);
	for (int ca = 1; ca <= t; ++ca)
	{
		int n;
		int answer;
		fscanf(infile, "%d\n", &n);
		int flag[10];
		memset(flag, '\0', sizeof(flag));
		long curn = 0; 
		for (int i = 1; i <= 100; ++i)
		{	
			curn = curn + n;
			long tmp = curn;
			if (tmp == 0) flag[0] = 1;
			else
			while (tmp > 0)
			{
				flag[tmp % 10] = 1;
				tmp /= 10;
			}
			answer = 1;
			for (int i = 0; i < 10; ++i)
				if (flag[i] == 0) 
				{
					answer = 0;
					break;
				}
			if (answer == 1)
			{
				fprintf(outfile, "Case #%d: %ld\n", ca, curn);
				break;
			}
		}
		if (answer == 0) fprintf(outfile, "Case #%d: INSOMNIA\n", ca);
	}
	return 0;
}