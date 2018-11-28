#include <iostream>
#include <cstdio>

using namespace std;

int D, P[1000];

int solve()
{
	int i, j, d, p;
	int ret, Pmax = 0;
	for(p = 0; p < D; p++)
	{
		if(P[p] > Pmax)
		{
			Pmax = P[p];
		}
	}
	ret = Pmax;
	for(i=1; i<Pmax; i++)
	{
		int time = i;
		for(p=0; p<D; p++)
		{
			time += ((P[p]-1)/i);
		}
		if(ret > time)
		{
			ret = time;
		}
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
		fscanf(in, "%d ", &D);
		for(i=0 ; i<D; i++)
		{
			fscanf(in, "%d ", &P[i]);
		}
		fprintf(out, "Case #%d: %d\n", t, solve());
	}
	fclose(in);
	fclose(out);
}
