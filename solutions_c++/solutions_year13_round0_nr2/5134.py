#include<stdio.h>
#define MAXN 120

int map[MAXN][MAXN];
int draw[MAXN][MAXN]={100,};

int main()
{
	int t,T;
	FILE * ip=fopen("B-large.in","r");
	FILE * op=fopen("B-large.out","w");

	fscanf(ip,"%d",&T);
	for(t=0;t<T;t++)
	{
		int N,M,i,j,max=-1,p=0;
		fscanf(ip,"%d%d",&N,&M);
		for(i=0;i<N;i++)
		{
			for(j=0;j<M;j++)
			{
				fscanf(ip,"%d",&map[i][j]);
				if(j==0)
					max=map[i][j];
				else
				{
					if(map[i][j]>max)
						max=map[i][j];
				}
				map[i][M+1]=max;
			}
		}

		for(i=0;i<N;i++)for(j=0;j<M;j++)
			draw[i][j]=100;
		for(j=0;j<M;j++)
		{
			max=map[0][j];
			for(i=0;i<N;i++)
				if(max<map[i][j])
					max=map[i][j];
			map[N+1][j]=max;
		}

		//
		for(i=0;i<N;i++)
		{
			max=map[i][M+1];
			for(j=0;j<M;j++)
				if(max<draw[i][j])
					draw[i][j]=max;
		}
		for(j=0;j<M;j++)
		{
			max=map[N+1][j];
			for(i=0;i<N;i++)
				if(max<draw[i][j])
					draw[i][j]=max;
		}
		//compare
		for(i=0;i<N;i++)for(j=0;j<M;j++)
			if(map[i][j]!=draw[i][j])
				p=1;
		if(p)
			fprintf(op,"Case #%d: NO\n",t+1);
		else
			fprintf(op,"Case #%d: YES\n",t+1);


	}

	return 0;
}