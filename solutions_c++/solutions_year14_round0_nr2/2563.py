#include <iostream>
using namespace std;
const double bonus = 2.0;


int main()
{
	FILE* fp = fopen("D:\\workspace\\codejam\\B-large.in","r");
	FILE* fo = fopen("D:\\workspace\\codejam\\result.txt","w");
	int tSize;
	fscanf(fp,"%d\n", &tSize);
	double C,F,X;

	for (int i = 1; i<=tSize; i++)
	{
		fscanf(fp,"%lf %lf %lf\n",&C,&F,&X);
		double S = bonus;						// Cookie speed
		double time = 0;
		while (C/S+X/(F+S) < X/S)
		{
			time += C/S;
			S += F;
		}
		time += X/S;
		fprintf(fo, "Case #%d: %0.7lf\n",i,time);
	}

	fclose(fp);
	fclose(fo);
	return 0;
}