#include <stdio.h>

int main()
{
	FILE *fp;
	FILE *fp_result;

	fp = fopen("D-small-attempt1.in", "r");
	fp_result = fopen("D-small-attempt_result.in", "w");

	int T;
	int numofcase = 1;
	fscanf(fp, "%d\n", &T);

	while(T--)
	{
		int X, R, C;
		fscanf(fp, "%d %d %d\n", &X, &R, &C);
		
		if(R * C % X != 0)
		{
			fprintf(fp_result, "Case #%d: RICHARD\n", numofcase++);
		}
		else if((R >= X - 1) && (C >= X - 1))
		{
			fprintf(fp_result, "Case #%d: GABRIEL\n", numofcase++);
		}
		else
		{
			fprintf(fp_result, "Case #%d: RICHARD\n", numofcase++);
		}

	}

	fclose(fp);
	fclose(fp_result);

}