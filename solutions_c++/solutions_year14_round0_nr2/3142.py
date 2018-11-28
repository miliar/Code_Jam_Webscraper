#include<cstdio>

using namespace std;

double find_time(double c, double f, double x)
{
	double cur = x / 2;
	double prev = cur + 1;
	int i = 0;
	while (cur < prev)
	{
		prev = cur;
		cur = prev - (x * f) / ((2 + i * f) * (2 + (i + 1) * f));
		cur += c / ( 2 + i * f);
		++ i;
	}
	return prev;
}

int main()
{
	int t;	
	double c, f, x;
	FILE * inf; 
	FILE * outf;	
	inf = fopen("in.txt","r");
	outf = fopen("out.txt","w");
	
	fscanf(inf, "%d", &t);
	for (int i = 0; i < t; ++ i)
	{
		fscanf(inf, "%lf%lf%lf", &c, &f, &x);
		fprintf(outf, "Case #%d: %.7f\n", i + 1, find_time(c, f, x));
	}
	fclose(outf);
}
