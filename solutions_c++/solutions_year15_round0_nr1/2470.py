#include <stdio.h>
#include <string.h>

#define MAXS 1100

char s[MAXS];

int main()
{
	FILE *infile, *outfile;
	infile = fopen("A-large.in", "r");
	outfile = fopen("output", "w");
	
	int tt;
	fscanf(infile, "%d\n", &tt);
	for (int ca = 1; ca <= tt; ++ca)
	{
		fprintf(outfile, "Case #%d: ", ca);
		memset(s, '\0', sizeof(s));
		int n;
		fscanf(infile, "%d %s", &n, s);
		int ans = 0, cnt = s[0] - '0';
		for (int i = 1; i <= n; ++i)
		{
		  if ((s[i] - '0' > 0) && (cnt < i))
		  {
		  	ans += i - cnt;
		  	cnt += i - cnt;
		  }
		  cnt += s[i] - '0';
		}
		  
		fprintf(outfile, "%d\n", ans);
	}
	
	return 0;
}
