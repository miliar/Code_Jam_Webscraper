#include <stdio.h>
#include <algorithm>
#include <memory.h>

#define M 1005
#define MOD 1000002013

#define Min(x,y) ((x)<(y)?(x):(y))

using namespace std;

FILE *in=fopen("A-small-attempt0.in","rt");
FILE *out=fopen("A-small-attempt0.out","wt");

__int64 X[2*M],sum1,sum2,mat[2*M][2*M],n;
int m;

struct data
{
	__int64 x1,x2,p;
	int y1,y2;
}a[M];

void input()
{
	int i;
	__int64 t;
	memset(mat,0,sizeof(mat));
	fscanf(in,"%I64d %d",&n,&m);
	for(i=1;i<=m;i++)
	{
		fscanf(in,"%I64d %I64d %I64d",&a[i].x1,&a[i].x2,&a[i].p);
		t=a[i].x2-a[i].x1;
		sum1+=a[i].p*(n*t-(t*t-t)/2);
		X[i*2-1]=a[i].x1;
		X[i*2]=a[i].x2;
		mat[a[i].x1][a[i].x2]+=a[i].p;
	}
//	sort(X+1,X+2*m+1);
//	n=unique(X+1,X+2*m+1)-X;
}

void process()
{
	int i,j,k,l;
	__int64 t;
	for(i=1;i<=n;i++)
	{
		for(j=i+1;j<=n;j++)
		{
			for(k=i+1;k<=j && mat[i][j]>0;k++)
			{
				for(l=j+1;l<=n && mat[i][j]>0;l++)
				{
					t=Min(mat[i][j],mat[k][l]);
					mat[i][j]-=t;
					mat[k][l]-=t;
					mat[k][j]+=t;
					mat[i][l]+=t;
				}
			}			
		}
	}
	for(i=1;i<=n;i++)
	{
		for(j=i+1;j<=n;j++)
		{
			t=j-i;
			sum2+=mat[i][j]*(n*t-(t*t-t)/2);
		}
	}
	fprintf(out,"%I64d",sum1-sum2);
}

int main()
{
	int t,i;
	fscanf(in,"%d",&t);
	for(i=1;i<=t;i++)
	{
		fprintf(out,"Case #%d: ",i);
		sum1=sum2=0;
		input();
		process();
		fprintf(out,"\n");
	}
	fclose(in);
	fclose(out);
	return 0;
}