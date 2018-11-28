#include<iostream>
#include<cstdio>
#include<algorithm>

using namespace std;


const int maxn = 1010;
int a[maxn];

int main()
{
	int t;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&t);
	for (int tt = 1; tt<=t; ++tt)
	{
		int n,ans = 0,ma = 0,tot = 0;
		scanf("%d",&n);
		for (int i=1; i<=n; ++i)
		{
			scanf("%d",&a[i]);
			if (a[i] > ma) ma = a[i];
		}
		ans = ma;
		sort(a+1,a+1+n);
		for (int i=1; i<=ma; ++i)
		{
			tot = 0;
			for (int j=1; j<=n; ++j)
				//if (a[j]>i)
					tot += ((a[j]-1) / i);
		//	printf("%d %d\n",i,tot);
			tot += i;
			if (tot < ans) ans = tot;
		}
		printf("Case #%d: %d",tt,ans);
		if (tt!=t) printf("\n");
	}
	return 0;
}
