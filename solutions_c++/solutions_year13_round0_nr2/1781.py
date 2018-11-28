#include<stdio.h>
FILE*in=fopen("input.txt","r");
FILE*out=fopen("output.txt","w");
int N,M,T;
int A[101][101];
int Maxx[101],Maxy[101];
int main()
{
	int t,i,j;
	int flag;
	fscanf(in,"%d",&T);
	for(t=1;t<=T;t++)
	{
		fprintf(out,"Case #%d: ",t);
		fscanf(in,"%d %d",&N,&M);
		for(i=1;i<=N;i++) Maxx[i]=0;
		for(i=1;i<=M;i++) Maxy[i]=0;
		for(i=1;i<=N;i++){
			for(j=1;j<=M;j++){
				fscanf(in,"%d",&A[i][j]);
				if(Maxx[i]<A[i][j]) Maxx[i]=A[i][j];
				if(Maxy[j]<A[i][j]) Maxy[j]=A[i][j];
			}
		}
		flag=0;
		for(i=1;i<=N;i++)
		{
			for(j=1;j<=M;j++)
			{
				if(A[i][j]<Maxx[i]&&A[i][j]<Maxy[j])
				{
					flag=1;
				}
			}
		}
		if(flag) fprintf(out,"NO\n");
		else fprintf(out,"YES\n");
	}
}