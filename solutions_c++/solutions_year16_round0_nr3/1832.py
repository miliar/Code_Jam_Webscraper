#include<cstdio>
#include<cstring>
#define N 1000
int n,m,ans,f[N];
void dfs(int x)
{
	int j;
	if (ans==m) return; 
	if (x>n-2)  
	{
		ans++;
		
		for (j=n;j>=1;j--)
		printf("%d",f[j]);
		for (j=2;j<=10;j++)
		printf(" %d",j+1);
		printf("\n");
		return;
	}
	dfs(x+1);
	if (f[x-1]==0)
	{
		f[x]=f[x-1]=1;
		dfs(x+1);
		f[x]=f[x-1]=0;
	}
} 
int main()
{
	int test,ii;
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d",&test);
	for (ii=1;ii<=test;ii++)
	{
		printf("Case #%d:\n",ii);
		scanf("%d%d",&n,&m);
		f[1]=f[2]=f[n-1]=f[n]=1;
		dfs(4);
	}
}
