#include <stdio.h>
#include <stdlib.h>

int main()
{
	FILE *fp;
	FILE *fp_result;

	fp = fopen("A-small-attempt1.in", "r");
	fp_result = fopen("A-small-attempt_result.in", "w");

	int T;
	fscanf(fp, "%d\n", &T);
	int numofcase = 1;

	while(T--)
	{
		int Smax;
		char str[1001] = {NULL,};
		int shyness[1001] = {0,};
		int count = 0;
		int need = 0;

		fscanf(fp, "%d %s\n", &Smax, str);
		for(int i = 0; i < Smax+1; i++)
		{
			shyness[i] = str[i] - 48;
			if(shyness[i] == 0)
			{
				continue;
			}
			if(i > count)
			{
				need += i - count;
				count += need;
			}

			count += shyness[i];
		}

		fprintf(fp_result, "Case #%d: %d\n", numofcase++, need);
	}

	fclose(fp);
}