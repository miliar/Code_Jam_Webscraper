#include <cstdio>
#include <algorithm>
using namespace std;
double a[1000], b[1000];

int main()
{
	freopen("d.in", "r", stdin);
	freopen("d.out", "w", stdout);
	int T, n, i, j, ans;
	scanf("%d", &T);
	for (int tt=1; tt<=T; ++tt)
	{
		scanf("%d", &n);
		for (i=0; i<n; ++i) scanf("%lf", a+i);
		for (i=0; i<n; ++i) scanf("%lf", b+i);
		sort(a, a+n);
		sort(b, b+n);
		ans=0;
		for (i=j=0; i<n && j<n; ++i)
		{
			while (j<n && a[j]<b[i]) ++j;
			if (j<n) ++ans, ++j;
		}
		printf("Case #%d: %d", tt, ans);
		ans=n;
		for (i=j=0; i<n && j<n; ++i)
		{
			while (j<n && b[j]<a[i]) ++j;
			if (j<n) --ans, ++j;
		}
		printf(" %d\n", ans);
	}
	return 0;
}

