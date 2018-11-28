#include <stdio.h>
#include <math.h>

double GetResult(double C, double F, double X);

int main()
{
	int T;
	double C,F,X;

	int i;
	
	FILE* fin=fopen("B-large.in" , "r");
	FILE* fout=fopen("output.out","w");
	
	fscanf(fin,"%d",&T);
	for(i=0 ; i<T ; i++)
	{
		fscanf(fin,"%lf",&C);
		fscanf(fin,"%lf",&F);
		fscanf(fin,"%lf",&X);
		
		fprintf(fout,"Case #%d: %lf\n",i+1,GetResult(C,F,X));		
	}

	fclose(fin);
	fclose(fout);

	return 0;
}

double GetResult(double C, double F, double X)
{
	double i = 2.0;
	double result=X/i;
	double preresult;
	double ftime=0;

	do
	{
		preresult = result;

		ftime += C/i;
		i+=F;
		result = ftime + X/i;
	}while(result < preresult);

	return preresult;
}