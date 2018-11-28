#include<cstdio>
#include<cstring>
#include<algorithm>
#define fo(i,a,b) for (int i = a;i <= b;i ++)

using namespace std;

const int maxn = 105;

int T,M,N,c[105][105],ans,sum;
char s[105][maxn];
int son[1000][26];

int build(int x)
{
	int tot = 1;
	memset(son,0,sizeof son);
	fo(i,1,c[x][0])
	{
		int now = c[x][i], len = strlen(s[now]+1);
		int cur = 1;
		fo(j,1,len)
		{
			if (!son[cur][s[now][j]-65]) son[cur][s[now][j]-65] = ++ tot;
			cur = son[cur][s[now][j]-65];
		}
	}
	return tot;
}

void dfs(int x)
{
	if (x > M)
	{
		int cnt = 0;
		fo(i,1,N)
		{
			if (!c[i][0]) return;
			cnt += build(i);
		}
		if (cnt > ans) ans = cnt, sum = 1;
		else if (cnt == ans) sum ++;
		return;
	}
	fo(i,1,N)
	{
		c[i][++c[i][0]] = x;
		dfs(x+1);
		c[i][0] --;
	}
}

int main()
{
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	scanf("%d",&T);
	fo(cs,1,T)
	{
		scanf("%d%d",&M,&N);
		fo(i,1,M) scanf("%s",s[i]+1);
		ans = 0, sum = 0;
		dfs(1);
		printf("Case #%d: ",cs);
		printf("%d %d\n",ans,sum);
	}
	return 0;
}
