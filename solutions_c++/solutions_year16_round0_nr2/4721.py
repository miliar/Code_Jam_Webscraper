#include <iostream>
#include <cstdio>

using namespace std;

int solve(const char *s)
{
	int ret = 0;
	char last = 0;
	for(;*s=='-' || *s=='+';s++)
		if(last != *s)
		{
			ret++;
			last = *s;
		}
	if(last == '+')
		return ret-1;
	return ret;
}

int main()
{
	FILE *in,*out;
	char line[1000];
	int T, t;
	int i, j;
	in = fopen("B.in","r");
	out = fopen("B.out","w+");
	fgets(line,999,in);
	sscanf(line,"%d",&T);
//	fscanf(in,"%d ",&T);
	for(t = 1; t <= T; t++)
	{
		fgets(line,999,in);
		fprintf(out, "Case #%d: %d\n", t, solve(line));
	}
	fclose(in);
	fclose(out);
}
