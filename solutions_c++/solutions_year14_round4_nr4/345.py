#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int f[5][1010][26],N[5];
int a[15];
int ans,tim,T,cas=0,n,m;
char s[1010][100];
bool vis[10];

void init(int x,int y)
{
	for (int i=0; i<26; i++) f[x][y][i]=0;
}

void insert(char S[],int x)
{
	int cur=0,k;
	for (int i=1; S[i]; i++)
	{
		k=S[i]-'A';
		if (f[x][cur][k]==0)
		{
			N[x]++;
			init(x,N[x]);
			f[x][cur][k]=N[x];
		}
		cur=f[x][cur][k];
	}
}

void check()
{
	for (int i=1; i<=n; i++) vis[i]=false;
	for (int i=1; i<=m; i++) vis[a[i]]=true;
	for (int i=1; i<=n; i++) if (!vis[i]) return;
	for (int i=1; i<=n; i++)
	{
		N[i]=0;
		init(i,0);
	}
	for (int i=1; i<=m; i++) insert(s[i],a[i]);
	int tmp=0;
	for (int i=1; i<=n; i++) tmp+=1+N[i];
	if (tmp>ans)
	{
		ans=tmp,tim=1;
		//for (int i=1; i<=m; i++) cout<<a[i]<<' '; cout<<endl;
	}
	else if (tmp==ans)
	{
		tim++;
		//for(int i=1; i<=m; i++) cout<<a[i]<<' '; cout<<endl;
	}

}

void dfs(int x)
{
	if (x==m+1)
	{
		check();
		return ;
	}
	for (int i=1; i<=n; i++)
	{
		a[x]=i;
		dfs(x+1);
	}
}

int main()
{
	freopen("D-small-attempt0.in","rb",stdin);
	freopen("test.out","wb",stdout);
	scanf("%d",&T);
	while (T--)
	{
		ans=tim=0;
		scanf("%d%d",&m,&n);
		for (int i=1; i<=m; i++) scanf("%s",s[i]+1);
		dfs(1);
		int tmp=1;
		for (int i=2; i<=n; i++) tmp*=n;
		//tim/=tmp;
		printf("Case #%d: %d %d\n",++cas,ans,tim);
	}
	return 0;
}
