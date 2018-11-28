#include <iostream>
#include <cstdio>

using namespace std;

const char *solve()
{
}

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
		char S[1010];
		int Smax, s;
		fscanf(in, "%d %1009s", &Smax, S);
		i=j=0;
		for(s=0; s<=Smax; s++)
		{
			i += S[s]-'0';
			if(i <= s)
			{
				j++;
				i++;
			}
		}
		fprintf(out, "Case #%d: %d\n", t, j);
	}
	fclose(in);
	fclose(out);
}
