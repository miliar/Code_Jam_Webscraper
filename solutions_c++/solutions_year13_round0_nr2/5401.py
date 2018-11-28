#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<string>
#include<cstdlib>
using namespace std;

#define debug(x) cout << #x << "=" << x << endl
#define sqr(x) ((x)*(x))

int tests,n,m;
int a[111][111];

int check(int x, int y)
{
	int p = 1, q = 1;
	for (int i=1;i<=n;i++) if (a[i][y]>a[x][y])
	{
		p = 0;
		break;
	}
	for (int j=1;j<=m;j++) if (a[x][j]>a[x][y])
	{
		q = 0;
		break;
	}
	return p || q;
}

int work()
{
	for (int i=1;i<=n;i++) for (int j=1;j<=m;j++)
		if (!check(i,j)) return 0;
	return 1;
}

int main()
{
	freopen("b2.in","r",stdin);
	freopen("b2.out","w",stdout);
	
	scanf("%d",&tests);
	for (int test=1;test<=tests;test++)
	{
		scanf("%d%d",&n,&m);
		for (int i=1;i<=n;i++) for (int j=1;j<=m;j++)
			scanf("%d",&a[i][j]);
		printf("Case #%d: ",test);
		if (work()) printf("YES\n");
		else printf("NO\n");
	}
	
	return 0;
}
