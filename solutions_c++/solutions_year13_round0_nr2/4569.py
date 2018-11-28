#include <stdio.h>
#include <memory.h>

#define N 105
#define Max(x,y) ((x)>(y)?(x):(y))

FILE *in=fopen("B-large.in","rt");
FILE *out=fopen("B-large.out","wt");

int n,m,map[N][N],maxd[2][N],a[N][N];

void input()
{
	int i,j;
	fscanf(in,"%d %d",&n,&m);
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=m;j++)
		{
			fscanf(in,"%d",&map[i][j]);
			a[i][j]=100;
		}
	}
}

void process()
{
	int i,j,k;
	memset(maxd,0,sizeof(maxd));
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=m;j++)
		{
			maxd[0][i]=Max(maxd[0][i],map[i][j]);
			maxd[1][j]=Max(maxd[1][j],map[i][j]);
		}
	}
	
	for(k=100;k>=1;k--)
	{
		for(i=1;i<=n;i++)
		{
			if(maxd[0][i]==k)
			{
				for(j=1;j<=m;j++) a[i][j]=maxd[0][i];
			}
		}

		for(j=1;j<=m;j++)
		{
			if(maxd[1][j]==k)
			{
				for(i=1;i<=n;i++) a[i][j]=maxd[1][j];
			}
		}
	}
	
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=m;j++)
		{
			if(a[i][j]!=map[i][j])
			{
				fprintf(out,"NO");
				return;
			}
		}
	}
	fprintf(out,"YES");
}

int main()
{
	int t,i;
	fscanf(in,"%d",&t);
	for(i=1;i<=t;i++)
	{
		fprintf(out,"Case #%d: ",i);
		input();
		process();
		fprintf(out,"\n");
	}
    fclose(in);
	fclose(out);
	return 0;
}