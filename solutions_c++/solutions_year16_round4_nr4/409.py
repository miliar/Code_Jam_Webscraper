#include <cstdio>
#include <cstring>
#include <algorithm>
#define fo(i,a,b) for (int i = a;i <= b;i ++)

int T,n,ans;
char s[35];
bool a[10][10],op[10],aw[10];

bool Check(int x)
{
	if (x > n) return 1;
	fo(j,1,n)
	{
		if (aw[j]) continue;
		bool boom = 1;
		fo(i,1,n)
			if (!op[i] && a[j][i])
			{
				boom = 0;
				op[i] = 1, aw[j] = 1;
				if (!Check(x+1)) return 0;
				op[i] = 0, aw[j] = 0;
			}
		if (boom) return 0;
	}
	return 1;
}

void DFS(int i,int j,int cur)
{
	if (i == n+1)
	{
		memset(op,0,sizeof op);
		memset(aw,0,sizeof aw);
		if (Check(1))
			if (cur < ans)ans = cur;
		return;
	}
	if (j > n)
	{
		DFS(i+1,1,cur);
		return;
	}
	if (a[i][j])
	{
		DFS(i,j+1,cur);
		return;
	}
	DFS(i,j+1,cur);
	a[i][j] = 1;
	DFS(i,j+1,cur+1);
	a[i][j] = 0;
}

int main()
{
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	scanf("%d",&T);
	fo(cs,1,T)
	{
		scanf("%d",&n);
		printf("Case #%d: ",cs);
		fo(i,1,n)
		{
			scanf("%s",s+1);
			fo(j,1,n) a[i][j] = (s[j] == '1');
		}
		ans = 2100000000;
		DFS(1,1,0);
		printf("%d\n",ans);
	}
	return 0;
}
