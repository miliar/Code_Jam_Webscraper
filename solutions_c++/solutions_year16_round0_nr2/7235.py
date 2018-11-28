#include <cstdio>
#include <cstring>

int main ()
{
	FILE *in=fopen("B-large.in","r");
	FILE *out=fopen("output.txt","w");

	int T,i,j,s,n,a[101];
	char c[101];

	fscanf (in,"%d",&T);
	for (int t=1;t<=T;t++)
	{
		fscanf (in,"%s",c);
		n=strlen(c);
		for (i=0;i<n;i++)
			a[i]=(c[i]=='-');
		s=0;

		for (i=n-1;i>=0;i--)
			if (a[i])
			{
				s++;
				for (j=i;j>=0;j--)
					a[j]=1-a[j];
			}
		
		fprintf (out,"Case #%d: %d\n",t,s);
	}
}