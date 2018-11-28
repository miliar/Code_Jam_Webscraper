#include <cstdio>
#include <algorithm>

int t, n, m, arr[101][101];

bool check(int x, int y)	{
	bool r1 = true,  r2 = true;
	for(int i=1;i<=n;i++) r1 &= (arr[i][y] <= arr[x][y]);
	for(int j=1;j<=m;j++) r2 &= (arr[x][j] <= arr[x][y]);
	return r1 || r2;
}

void solve(int cas)	{
	bool ret = true;
	scanf("%d%d",&n,&m);
	for(int i=1;i<=n;i++) for(int j=1;j<=m;j++) scanf("%d",&arr[i][j]);
	for(int i=1;i<=n;i++)	{
		for(int j=1;j<=m;j++)	{
			ret &= check(i,j);
		}
	}
	printf("Case #%d: ", cas);
	if(ret) printf("YES\n");
	else printf("NO\n");
}

int main()	{
	scanf("%d",&t);
	for(int ct=1;ct<=t;ct++)	{
		solve(ct);
	}
	return 0;
}
