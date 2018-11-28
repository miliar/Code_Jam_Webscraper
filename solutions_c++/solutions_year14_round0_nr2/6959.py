#include <stdio.h>
#include <math.h>
using namespace std;

const char* fname = "file2.in";
const char* fnameo = "file2o.in";

double timeTaken(double c, double f, double x);

int main()
{
	int i = 0;
	double T, C, F, X, R = 2.0, tim = 0.0;
	FILE *file, *fileo;
	file = fopen(fname, "r+");
	fileo = fopen(fnameo, "w+");
	fscanf(file, "%lf\n", &T);
	while(!feof(file) && i < T)
	{
		fscanf(file, "%lf %lf %lf\n", &C, &F, &X);
		tim = timeTaken(C, F, X);
		fprintf(fileo, "Case #%d: %lf\n", i + 1, tim);
		printf("Case #%d: %lf\n", i + 1, tim);
		i++;
	}
	
	fclose(file);
	fclose(fileo);
	return 0;
}

double timeTaken(double c, double f, double x)
{
	double num = (f + 2)*(x - c) - 2*x;
	double den = f*c;
	double frac = num/den;
	double time_taken = 0;
	int n = 0;
	
	if(frac < 0)
	{
		time_taken = x/2.0;
	}
	else
	{
		n = ceil(frac);
		for(int i = 0; i < n; i++)
		{
			time_taken = time_taken + c/(2 + i*f);
		}
		time_taken = time_taken + x/(2 + n*f);
	}
	
	return time_taken;
}
