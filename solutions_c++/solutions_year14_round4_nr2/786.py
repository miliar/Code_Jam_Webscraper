#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int Maxn=1002, INF=1<<30;
int a[Maxn], f[Maxn], g[Maxn];

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int T, i, j, n, ans;
	scanf("%d", &T);
	for (int tt=1; tt<=T; ++tt)
	{
		scanf("%d", &n);
		for (i=1; i<=n; ++i) scanf("%d", a+i);
		memset(f, 0, sizeof f);
		for (i=2; i<=n; ++i)
			for (j=1; j<i; ++j)
				if (a[j]>a[i]) ++f[i];
		memset(g, 0, sizeof g);
		for (i=n-1; i; --i)
			for (j=n; j>i; --j)
				if (a[j]>a[i]) ++g[i];
		//for (i=1; i<=n; ++i) printf("%d ", f[i]); printf("\n");
		//for (i=1; i<=n; ++i) printf("%d ", g[i]); printf("\n");
		ans=0;
		for (i=1; i<=n; ++i) ans+=min(f[i],g[i]);
		printf("Case #%d: %d\n", tt, ans);
	}
	return 0;
}

