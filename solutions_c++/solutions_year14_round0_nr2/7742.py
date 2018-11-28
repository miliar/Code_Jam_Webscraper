#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

void inputf(FILE *in, FILE *out);
void process(FILE *in, FILE *out, double C, double F, double X);

int main(void)
{
	FILE *in=fopen("input.in", "r");
	FILE *out=fopen("output.out", "w");

	int testcase;
	fscanf(in,"%d", &testcase);
	for(int i=0;i<testcase;i++)
	{
		fprintf(out,"Case #%d: ", i+1);
		inputf(in,out);
	}
	
	fclose(in);
	fclose(out);

	return 0;
}

void inputf(FILE *in, FILE *out)
{
	double C,F,X;
	fscanf(in,"%lf %lf %lf", &C, &F, &X);

	process(in,out,C,F,X);

	return;
}

void process(FILE *in, FILE *out, double C, double F, double X)
{
	double produce=2;
	double second;
	double secsum=0;

	while(1)
	{
		second=C/produce;
		if(second+(X/(produce+F))>=X/produce)
			break;
		else
		{
			secsum+=second;
			produce+=F;
		}
	}
	secsum+=X/produce;

	fprintf(out,"%0.7lf\n", secsum);

	return;
}
