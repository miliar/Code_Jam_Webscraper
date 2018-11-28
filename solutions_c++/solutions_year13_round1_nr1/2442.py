#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

#define FILE_IN "A-small-attempt1.in"
#define FILE_OUT "A-small-attempt1.out"

int main()
{
	FILE *in = fopen(FILE_IN, "r");
	FILE *out = fopen(FILE_OUT, "w");

	int case_num, i=0;
	fscanf(in, "%d", &case_num);
	while(i<case_num)
	{
		double sNum, eNum, oNum = 0, total, iterator;
		fscanf(in, "%lf %lf", &sNum, &eNum);

		while(eNum>0.0f)
		{
			eNum = eNum - (2.0f*sNum+1.0f);
			
			if(eNum>=0.0f)
				oNum++;
			sNum+=2.0f;
		}
		//printf("Case #%d: %lf\n", i+1, oNum);
		fprintf(out, "Case #%d: %.lf\n", i+1, oNum);
		i++;
	}
	fclose(in);
	fclose(out);
	//getchar();
	return 0;
}