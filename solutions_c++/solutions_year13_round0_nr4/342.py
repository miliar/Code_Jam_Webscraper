#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

int T;
int hk[256];
bool v[1048576],flag;
int c[256];
int a[256][256];
int n,k,tmp;
int stk[32];
int t[32];

void dfs(int dep,int st)
{
	if (flag) return;
	if (v[st]) return;
	v[st]=true;
	if (dep>n)
	{
		flag=true;
		return;
	}
	for (int i=0;i<n;i++)
		if ((((1<<i)&st)==0) && hk[t[i]]>0)
		{
			stk[dep]=i+1;
			hk[t[i]]--;
			for (int j=0;j<c[i];j++) hk[a[i][j]]++;
			dfs(dep+1,st|(1<<i));
			if (flag) return;
			for (int j=0;j<c[i];j++) hk[a[i][j]]--;
			hk[t[i]]++;
		}
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
    scanf("%d",&T);
    for (int ww=1;ww<=T;ww++)
	{
		printf("Case #%d:",ww);
		scanf("%d%d",&k,&n);
		memset(hk,0,sizeof(hk));
		for (int i=1;i<=k;i++)
		{
			scanf("%d",&tmp);
			hk[tmp]++;
		}
		for (int i=0;i<n;i++)
		{
			scanf("%d%d",t+i,c+i);
			for (int j=0;j<c[i];j++) scanf("%d",a[i]+j);
		}
		memset(v,false,sizeof(v));
		flag=false;
		dfs(1,0);
		if (flag)
		{
			for (int i=1;i<=n;i++) printf(" %d",stk[i]);
			printf("\n");
		}
		else printf(" IMPOSSIBLE\n");
	}
    return 0;
}
