#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	FILE *in,*out;
//	char line[1000];
	int T, t;
	int i, j;
	in = fopen("A.in","r");
	out = fopen("A.out","w+");
//	fgets(line,999,in);
//	sscanf(line,"%d",&T);
	fscanf(in,"%d ",&T);
	for(t = 1; t <= T; t++)
	{
		int N;
		fscanf(in, "%d ", &N);
		if(!N)
		{
			fprintf(out, "Case #%d: INSOMNIA\n", t);
			continue;
		}
		
		int s = N;
		for(i=0;i!=0x3FF;N+=s)
		{
			for(j=N;j;j/=10)
				i |= (1<<(j%10));
		}
		fprintf(out, "Case #%d: %d\n", t, N-s);
	}
	fclose(in);
	fclose(out);
}
