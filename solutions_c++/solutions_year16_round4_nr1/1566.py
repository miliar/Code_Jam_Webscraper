#include <cstdio>

int n,m,f,a[3],b[20];
char c[4]="PRS";

int win (int x, int y)
{
	if (x==y) return -1;
	if ((x&&x==y+1)||(x==0&&y==2)) return x;
	return y;
}

FILE *in=fopen("A-small-attempt2.in","r");
FILE *out=fopen("output.txt","w");

void go (int x)
{
	int i;

	if (f)
		return;
	if (x==m)
	{
		for (i=m-1;i;i--)
		{
			x=win(b[i*2],b[i*2+1]);
			if (x<0)
				break;
			b[i]=x;
		}
		if (!i)
		{
			f=1;
			for (i=m;i<m*2;i++)
				fprintf (out,"%c",c[b[i]]);
		}
	}
	else
	{
		for (i=0;i<3;i++)
			if (a[i])
			{
				a[i]--;
				b[x+m]=i;
				go (x+1);
				a[i]++;
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
		int i,j;

		fscanf (in,"%d%d%d%d",&n,a+1,a+0,a+2);
		m=1<<n;
		f=0;
		go (0);
		if (!f) fprintf (out,"IMPOSSIBLE");
		fprintf (out,"\n");
	}
	return 0;
}