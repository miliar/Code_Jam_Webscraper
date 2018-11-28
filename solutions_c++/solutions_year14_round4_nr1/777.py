#include <cstdio>
#include <algorithm>
using namespace std;
int a[10001];

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int T, n, x, i, j, cnt;
	scanf("%d", &T);
	for (int tt=1; tt<=T; ++tt)
	{
		scanf("%d%d", &n, &x);
		for (i=0; i<n; ++i) scanf("%d", a+i);
		sort(a, a+n);
		cnt=0;
		for (i=n-1, j=0; i>=j; --i)
		{
			++cnt;
			if (a[i]+a[j]<=x) ++j;
		}
		printf("Case #%d: %d\n", tt, cnt);
	}
	return 0;
}

