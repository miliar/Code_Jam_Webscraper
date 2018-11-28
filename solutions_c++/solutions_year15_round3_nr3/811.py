# include <iostream>
# include <cstdio>
# include <string.h> 
using namespace std;
int C,D,V;
int f[1001],g[1001];
int w[1001],ans;
void init()
{
	int i,j;
	scanf("%d %d %d",&C,&D,&V);
	for (i=1;i<=D;i++)scanf("%d",&w[i]);
	memset(f,0,sizeof(f));f[0]=1;
} 
void dfs(int x,int s)
{
	if (x>D)return;
	int i;
	for (i=0;i<=C;i++){
		f[s+i*w[x]]=1;//cout<<s+i*w[x]<<endl;
		dfs(x+1,s+i*w[x]);
	}
}
void work()
{
	int i,j,k;
	ans=0;dfs(1,0);
//	for (i=1;i<=V;i++)printf("%d ",f[i]);
//	printf("\n");
	for (j=1;j<=V;j++)
	{
		if (f[j]==0){
			for (i=0;i<=V;i++)g[i]=f[i];
			for (i=1;i<=C;i++)
			    for (k=0;k<=V;k++)
				    if (f[k] && k+i*j<=V)g[k+i*j]=1; 
			ans++;
			for (i=0;i<=V;i++)f[i]=g[i];
	//		for (k=1;k<=V;k++)cout<<f[k]<<' ';
	//		cout<<endl;
		}
		
	}
	
}
int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int i,q;
	scanf("%d",&q);
	for (i=1;i<=q;i++)
	{
		init();
		work();
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
} 
