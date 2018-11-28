#include<stdio.h>
#include<stdlib.h>
int main()
{
	FILE *fin  = fopen ("A-large.in", "r");
    FILE *fout = fopen ("A-large.out", "w");
	int t,i,j,smax,c,n;
	char s[1005];
	fscanf(fin,"%d",&t);
	for(j=1;j<=t;j++)
	{
		c=0;
		fscanf(fin,"%d %s",&smax,s);
		for(i=0;i<=smax;i++)
		s[i]=s[i]-'0';
		n=s[0];
		for(i=1;i<=smax;i++)
		{
			if(n<i)
			{
				c+=(i-n);
				n+=(i-n);
			}
			n+=s[i];
		}
		fprintf(fout,"Case #%d: %d\n",j,c);
	}
	return 0;
}
