#include <cstring>
#include <cstdio>
#include <algorithm>

int T,t,n,i,j,s,e,c;
char a[1002],b[2004];

int main ()
{
	FILE *in=fopen ("A-large.in","r");
	FILE *out=fopen ("output.txt","w");

	fscanf (in,"%d",&T);
	printf ("%d ",t);
	for (t=1;t<=T;t++)
	{
		int i,j;
		fscanf (in,"%s",a);
		printf ("%s ",a);
		n=strlen(a);
		s=e=n,b[s]=a[0];

		for (i=1;i<n;i++)
		{
			c=0;
			for (j=i+1;j<n;j++)
				if (a[j]>a[i])
					c=1;
			if (a[i]>=b[s])
				b[--s]=a[i];
			else
				b[++e]=a[i];
		//	for (j=s;j<=e;j++)
			//	printf ("%c",b[j]);printf ("\n");
		}

		fprintf (out, "Case #%d: ",t);
		for (i=s;i<=e;i++)
			fprintf (out,"%c",b[i]);
		fprintf (out,"\n");
	}
}