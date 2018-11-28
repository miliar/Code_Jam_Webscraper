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
	freopen("B-large.in", "r", stdin);
	freopen("b-large.out", "w", stdout);
	scanf("%d", &t);
	for (int cas=1; cas<=t; cas++)
	{
		int n,a[NN];
		scanf("%d",&n);
		for (i=0; i<n; i++) scanf("%d",&a[i]);
		int ans=0;
		for (i=0; i<n; i++)
		{
			int bnum=0;
			for (j=i-1; j>=0; j--) if (a[j]>a[i]) bnum++;
			int bnum2=0;
			for (j=i+1; j<n; j++) if (a[j]>a[i]) bnum2++;
			if (bnum<bnum2) ans+=bnum;
			else ans+=bnum2;
		}
		printf("Case #%d: %d\n", cas, ans);
	}
	return 0;
}

