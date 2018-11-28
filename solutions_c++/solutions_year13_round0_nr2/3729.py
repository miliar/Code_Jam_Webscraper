#include<stdio.h>

int lawn[100][100], N, M, max;

int checkrows(int c,int k);
int checkcols(int r,int k);

int main()
{
	int t=1,T,i,j;
	scanf("%d",&T);
	while(t<=T)
	{
		scanf("%d %d\n",&N,&M);
		for(i=0;i<N;i++)
			for(j=0;j<M;j++)
				scanf("%d",&lawn[i][j]);
		max=-1;
		for(i=0;i<N;i++)
			for(j=0;j<M;j++)
				if(lawn[i][j]>max)
					max=lawn[i][j];
		int res=1;
		for(i=0;i<N;i++)
			for(j=0;j<M;j++)
			{
				if(lawn[i][j]<max && checkcols(i,j)!=0 && checkrows(j,i)!=0)
					res=0;
			}
		if(res==1)
			printf("Case #%d: YES\n",t);
		else
			printf("Case #%d: NO\n",t);
		t++;
	}
}

int checkrows(int c,int k)
{
	int count=0,i;
	for(i=0;i<N;i++)
		if(lawn[i][c] > lawn[k][c])
			count++;
	return count;
}

int checkcols(int r,int k)
{
	int count=0, i;
	for(i=0;i<M;i++)
		if(lawn[r][i]>lawn[r][k] )
			count++;
	return count;
}