#include<stdio.h>
#define OUT out

int main()
{
	int testcase;
	FILE *in = fopen("B-large.in","r");
	FILE *out = fopen("output.txt","w");
	fscanf(in,"%d",&testcase);
	for(int T = 1; T <= testcase; T++)
	{
		double C, F, X;
		fscanf(in,"%lf %lf %lf",&C, &F, &X);
		double v = 2.0;
		double temp = 0;
		double result = X / v;
		for(int i = 1; ; i++)
		{
			temp += C / v;
			v += F;
			if(temp + X / v > result) break;
			else result = temp + X / v;
		}
		
		fprintf(OUT,"Case #%d: %lf\n",T,result);
	}
	fclose(in);
	fclose(out);
	return 0;
}