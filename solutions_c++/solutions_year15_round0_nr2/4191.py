#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

int p[2000];
int f[1100][1100];
int n;

int calc(int lim)
{
	int ans = 0;
	for (int i=0;i<n;++i)
	{
		int x = p[i];
		ans += f[x][lim];
	}
	return ans;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	//freopen("x.in","r",stdin);
	memset(f, 0, sizeof(f));
	for (int j=1;j<=1000;++j)
	{
		for (int i=0;i<=j;++i)
			f[i][j] = 0;
		for (int i=j+1;i<=1000;++i)
		{
			f[i][j] = 999999;
			for (int k=1;k<i;++k)
				f[i][j] = min(f[i][j], f[k][j] + f[i - k][j] + 1);
		}
	}
	int T;
	scanf("%d", &T);
	for (int ii=1;ii<=T;++ii)
	{
		printf("Case #%d: ", ii);
		scanf("%d", &n);
		for (int i=0;i<n;++i)
			scanf("%d", &p[i]);
		int ans = 999999999;
		for (int res=1;res<=1000;++res)
			ans = min(ans, res + calc(res));
		printf("%d\n", ans);
	}
}