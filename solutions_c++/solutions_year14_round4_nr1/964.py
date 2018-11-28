#include <cstdio>
#include <cstring>
#include <set>
#include <algorithm>
#include <cmath>
#include <cctype>
using namespace std;
#define NN 100008

int main()
{
	int t, i, j;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &t);
	for (int cas=1; cas<=t; cas++)
	{
		int n,x,a[NN];
		scanf("%d%d",&n,&x);
		for (i=0; i<n; i++) scanf("%d",&a[i]);
		sort(a,a+n);
		j=n-1;
		int ans=0;
		for (i=0; i<=j; i++)
		{
			while (j>i && a[i]+a[j]>x) j--, ans++;
			if (j>i) j--;
			ans++;
		}
		printf("Case #%d: %d\n", cas, ans);
	}
	return 0;
}

