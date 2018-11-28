#include <iostream>
#include <cstdio>
#include <set>

using namespace std;

set<double> A,B;
int N;

int solve1()
{
	set<double>::iterator al = A.begin();
	set<double>::iterator bl = B.begin();
	set<double>::reverse_iterator ah = A.rbegin();
	set<double>::reverse_iterator bh = B.rbegin();
	int ret = 0;
	while(al != A.end() && ah != A.rend() && *al <= *ah)
	{
		if(*ah > *bh)
		{
			ret++;
			ah++;
		}
		else
		{
			al++;
		}
		bh++;
	}
	return ret;
}

int solve2()
{
	set<double>::iterator bl = B.begin();
	set<double>::reverse_iterator ah = A.rbegin();
	set<double>::reverse_iterator bh = B.rbegin();
	int ret = 0;
	while(ah != A.rend())
	{
		if(*ah > *bh)
		{
			ret++;
			bl++;
		}
		else
		{
			bh++;
		}
		ah++;
	}
	return ret;
}

int main()
{
	FILE *in,*out;
//	char line[1000];
	int T, t;
	int i, j;
	in = fopen("D.in","r");
	out = fopen("D.out","w+");
//	fgets(line,999,in);
//	sscanf(line,"%d",&T);
	fscanf(in,"%d ",&T);
	for(t = 1; t <= T; t++)
	{
		double tmp;
		fscanf(in,"%d ",&N);
		A.clear();
		for(i = 0; i < N; i++)
		{
			fscanf(in, "%lf ", &tmp);
			A.insert(tmp);
		}
		B.clear();
		for(i = 0; i < N; i++)
		{
			fscanf(in, "%lf ", &tmp);
			B.insert(tmp);
		}
		fprintf(out, "Case #%d: %d %d\n", t, solve1(), solve2());
	}
	fclose(in);
	fclose(out);
}
