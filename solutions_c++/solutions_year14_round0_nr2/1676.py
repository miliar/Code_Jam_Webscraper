#include <iostream>
#include <cstdio>

using namespace std;

double C, F, X;

double solve()
{
	double rate = 2;
	double ret = X/rate;
	double time=0;
	while(time<ret)
	{
		time += (C/rate);
		rate += F;
		if( (time+(X/rate)) < ret)
			ret = (time+(X/rate));
	}
	return ret;
}

int main()
{
	FILE *in,*out;
//	char line[1000];
	int T, t;
	int i, j;
	in = fopen("B.in","r");
	out = fopen("B.out","w+");
//	fgets(line,999,in);
//	sscanf(line,"%d",&T);
	fscanf(in,"%d ",&T);
	for(t = 1; t <= T; t++)
	{
		fscanf(in, "%lf %lf %lf ", &C, &F, &X);
		fprintf(out, "Case #%d: %.7lf\n", t, solve());
	}
	fclose(in);
	fclose(out);
}
