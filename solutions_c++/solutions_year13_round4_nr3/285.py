#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

int N;
int A[2000];
int B[2000];
int res[2000];

int solve(int index)
{
	int i,j;
	if(index==N)
		return 1;
	index++;
	for(i=0; i<N; i++)
	{
		if(res[i]<index || A[i]>index || B[i]>index)
			continue;
		int a=0;
		for(j=0;j<i;j++)
		{
			if(res[j]<index && A[j]>a)
				a=A[j];
		}
		if(A[i] != a+1)
			continue;
		int b=0;
		for(j=i+1;j<N;j++)
		{
			if(res[j]<index && B[j]>b)
				b=B[j];
		}
		if(B[i] != b+1)
			continue;
		res[i]=index;
		if(solve(index))
			return 1;
		res[i]=10000;
	}
	return 0;
}

int main()
{
	FILE *in,*out;
//	char line[1000];
	int T, t;
	int i, j, tmp;
	in = fopen("C.in","r");
	out = fopen("C.out","w+");
//	fgets(line,999,in);
//	sscanf(line,"%d",&T);
	fscanf(in,"%d ",&T);
	for(t = 1; t <= T; t++)
	{
//		fgets(line,999,in);//empty line
		fscanf(in,"%d ",&N);
		for(i=0;i<N;i++)
			fscanf(in,"%d ",&A[i]);
		for(i=0;i<N;i++)
			fscanf(in,"%d ",&B[i]);
		for(i=0;i<N;i++)
			res[i] = 10000;
		solve(0);
		fprintf(out, "Case #%d:", t);
		for(i=0;i<N;i++)
			fprintf(out, " %d", res[i]);
		fprintf(out, "\n");
	}
	fclose(in);
	fclose(out);
}
