#include <cstdio>

FILE *in=fopen("B-small-attempt2.in","r");
FILE *out=fopen("output.txt","w");

int n,m,b[210],d[20];
double a[210],s,mx;

int check (int x)
{
	int i,c=0;
	for (i=0;i<n;i++)
		b[i]=x%2,c+=b[i],x/=2;
	return c;
}

void go (int x, int c, double p)
{
	if (x==n&&c==m/2)
		s+=p;
	else if (x<n)
	{
		if (b[x]==0)
			go (x+1,c,p);
		else
		{
			if (c<m/2)
				go (x+1,c+1,p*a[x]);
			go (x+1,c,p*(1-a[x]));
		}
	}
}

int main ()
{
	int t,T;
	fscanf (in,"%d",&T);
	for (t=1;t<=T;t++)
	{
		fprintf (out,"Case #%d: ",t);
		int i,j,k;

		fscanf (in,"%d%d",&n,&m);
		for (i=0;i<n;i++)
			fscanf (in,"%lf",a+i);
		mx=0;
		for (i=0;i<1<<n;i++) if (check(i)==m)
		{
			s=0;k=0;
			go (0,0,1);
			//for (int j=0;j<n;j++) printf ("%d ",b[j]); printf (" : %lf\n",s);
			if (mx<s) mx=s;
		}
		fprintf (out, "%lf\n",mx);
	}
	return 0;
}