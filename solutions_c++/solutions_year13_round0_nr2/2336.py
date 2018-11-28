#include<stdio.h>
#include<stdlib.h>
#define PAUSE system("pause")
#define MAX 100
int N,M;
int A[MAX][MAX];
int L[MAX][MAX];
main()
{
//	freopen("B_large.in","r",stdin);
//	freopen("B_large_out.txt","w",stdout);
	int Test,Case,i,j,k;
	scanf("%d",&Test);
	for(Case=1;Case<=Test;Case++)
	{
		scanf("%d %d",&N,&M);
		for(i=0;i<N;i++)
			for(j=0;j<M;j++)
			{
				scanf("%d",&A[i][j]);
				L[i][j]=MAX;
			}
		for(i=0;i<N;i++)
		{
			for(j=k=0;j<M;j++)
				if(k<A[i][j]) k=A[i][j];
			for(j=0;j<M;j++)
				if(L[i][j]>k) L[i][j]=k;
		}
		for(i=0;i<M;i++)
		{
			for(j=k=0;j<N;j++)
				if(k<A[j][i]) k=A[j][i];
			for(j=0;j<N;j++)
				if(L[j][i]>k) L[j][i]=k;
		}
		for(i=0,k=1;i<N;i++)
			for(j=0;j<M;j++)
				if(L[i][j]!=A[i][j]) k=0;
		printf("Case #%d: ",Case);
		puts(k?"YES":"NO");
	}
}
