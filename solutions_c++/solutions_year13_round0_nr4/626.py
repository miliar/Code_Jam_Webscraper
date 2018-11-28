// Pure DP
#include<stdio.h>
#include<stdlib.h>
#define PAUSE system("pause")
#define AMOUNT 201
#define MAX 20
#define State (1<<20)
int Init[AMOUNT];
int Count[AMOUNT];
int key[MAX],size[MAX];
int attain[MAX][MAX*2];
bool Avail[State];
int Step[State][MAX];
main()
{
//	freopen("D_small.in","r",stdin);
//	freopen("D_small_out.txt","w",stdout);
	int Test,Case,i,j,t,c,K,N;
	scanf("%d",&Test);
	for(Case=1;Case<=Test;Case++)
	{
		scanf("%d %d",&K,&N);
		for(i=0;i<AMOUNT;i++) Init[i]=0;
		for(i=0;i<K;i++)
		{
			scanf("%d",&j);
			Init[j]++;
		}
		for(i=0;i<N;i++)
		{
			scanf("%d",key+i);
			scanf("%d",size+i);
			for(j=0;j<size[i];j++)
				scanf("%d",attain[i]+j);
		}
		for(i=0;i<(1<<N);i++) Avail[i]=0;
		Avail[0]=1;
		for(i=0;i<(1<<N);i++)
		{
			if(Avail[i]==0) continue;
			for(j=0;j<AMOUNT;j++) Count[j] = Init[j];
			for(c=j=0;j<N;j++)
				if(i & (1<<j))
				{
					c++ ,Count[ key[j] ]--;
					for(t=0;t<size[j];t++)
						Count[ attain[j][t] ]++;
				}
			for(j=0;j<N;j++)
			{
				t = i|(1<<j);
				if(i<t && Count[key[j]])
				{
					if(Avail[t])
					{
						int z;
						for(z=0;z<c;z++)
							if(Step[t][z]!=Step[i][z]) break;
						if(Step[t][z]<Step[i][z]) continue;
					}
					Avail[t]=1;
					for(int r=0;r<c;r++) Step[t][r]=Step[i][r];
					Step[t][c]=j;
				}
			}
		}
		printf("Case #%d:",Case);
		
		/*
		puts("");
		for(i=0;i<(1<<N);i++)
			if(Avail[i]) printf("%d  ",i);
		puts("");
		*/
		
		if(Avail[(1<<N)-1])
		{
			for(i=0;i<N;i++) printf(" %d",Step[(1<<N)-1][i]+1);
			puts("");
		}
		else puts(" IMPOSSIBLE");
	}
}
