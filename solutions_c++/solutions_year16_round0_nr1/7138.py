#include <cstdio>

int main ()
{
	FILE *in=fopen("A-large.in","r");
	FILE *out=fopen("output.txt","w");

	int T,i,j,n,c,k,a[10];

	fscanf (in,"%d",&T);
	for (int t=1;t<=T;t++)
	{
		for (i=0;i<10;a[i++]=0);
		fscanf (in,"%d",&n);
		for (i=1;n;i++)
		{
			k=i*n;
			while (k)
				a[k%10]=1,k/=10;
			for (j=0;j<10;j++)
				if (!a[j]) break;
			if (j>9) break;
		}

		if (n==0)
			fprintf (out,"Case #%d: INSOMNIA\n",t);
		else
			fprintf (out,"Case #%d: %d\n",t,i*n);
	}
}