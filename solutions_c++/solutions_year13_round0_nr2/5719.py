#include<stdio.h>
#define MAX 100
int a[MAX][MAX];
int main()
{
	FILE *fin=fopen("B-small-attempt0.in","r");
	FILE *fout=fopen("B-small-attempt0.out","w");
	int T,t,flag;
	int i,j,k;
	int N,M;
	fscanf(fin,"%d",&T);
	for(t=1;t<=T;t++)
	{
		flag=0;
		fscanf(fin,"%d",&N);
		fscanf(fin,"%d",&M);
		for(i=0;i<N;i++)
			for(j=0;j<M;j++)
				fscanf(fin,"%d",&a[i][j]);
		for(i=0;i<N;i++)
		{
			for(j=0;j<M;j++)
			{
				if(a[i][j]==1)
				{
					for(k=0;k<M;k++)
						if(a[i][k]!=1)
						{
							flag=1; break;
						}
					if(flag)
					{
						flag=0;
						for(k=0;k<N;k++)
							if(a[k][j]!=1)
							{
								flag=1;break;
							}
					}
				}
				if(flag)
					break;
			}
			if(flag)
				break;
		}
		if(flag==0)
			fprintf(fout,"Case #%d: YES\n",t);
		else
			fprintf(fout,"Case #%d: NO\n",t);
	}
	return 0;
}
