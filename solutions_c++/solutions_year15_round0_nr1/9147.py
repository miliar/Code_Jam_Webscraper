#include <stdio.h>
int t, n, i, j, s, res;
char c;
int main()
{
	FILE *ifp=fopen("input.txt", "r");
	FILE *ofp=fopen("output.txt", "w");
	fscanf(ifp, "%d", &t);
	for (i=1; i<=t;i++)
	{
		fscanf(ifp, "%d ", &n);
		res=0;
		s=0;
		c=fgetc(ifp);
		s+=c-'0';
		for (j=1;j<=n;j++)
		{
			if (j>s)
			{
				res+=j-s;
				s=j;
			}
			c=fgetc(ifp);
			s+=c-'0';
		}
		fprintf(ofp, "Case #%d: %d\n", i, res);
	}
	fclose(ifp);
	fclose(ofp);
	return 0;
}