#include <iostream>
#include <cstdio>
#include <set>

using namespace std;

int A,B,K;

long long solve()
{
	long long ret = 0;
	int i,j;
	for(i=0;i<A;i++)
	{
		for(j=0;j<B;j++)
			if((i&j)<K)
				ret++;
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
	cout<<t<<endl;
//		fgets(line,999,in);//empty line
		fscanf(in,"%d %d %d ", &A, &B, &K);
		fprintf(out, "Case #%d: %lld\n",t,solve());
	}
	fclose(in);
	fclose(out);
}
