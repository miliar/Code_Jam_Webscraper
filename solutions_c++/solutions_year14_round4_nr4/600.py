#include<stdio.h>
#include<string.h>
int N,M;
struct LIST
{
	char a[11];
	int len;
}list[11];
int A[10][101];
int C[10];
int Max=-1,Count;
struct TREE
{
	int c[30];
}tree[101];
void check()
{
	int i,j,k,x;
	for(i=1;i<=M;i++) if(C[i]==0) return;
	int K=0,c=0;
	for(i=1;i<=M;i++)
	{
		K=0;
		for(j=0;j<C[i];j++)
		{
			x=0;
			for(k=1;k<=list[A[i][j]].len;k++)
			{
				if(!tree[x].c[list[A[i][j]].a[k]-'A'])
				{
					K++;
					tree[x].c[list[A[i][j]].a[k]-'A']=K;
					x=K;
				}
				else x=tree[x].c[list[A[i][j]].a[k]-'A'];
			}
		}
		c+=K;
		for(j=0;j<=K;j++) memset(tree[j].c,0,sizeof(tree[j].c));
	}
	c+=M;
	if(Max<c) Max=c,Count=1;
	else if(Max==c) Count++;
}
void dfs(int x)
{
	if(x==N+1)
	{
		check();
		return;
	}
	int i;
	for(i=1;i<=M;i++)
	{
		A[i][C[i]++]=x;
		dfs(x+1);
		A[i][--C[i]]=0;
	}
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,t,i;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%d %d",&N,&M);
		for(i=1;i<=N;i++)
		{
			scanf("%s",&list[i].a[1]);
			list[i].len=strlen(&list[i].a[1]);
		}
		Max=-1,Count=0;
		dfs(1);
		printf("Case #%d: %d %d\n",t,Max,Count);
	}
}