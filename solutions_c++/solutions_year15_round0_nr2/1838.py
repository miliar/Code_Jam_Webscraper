#include <cstdio>
#include <algorithm>
using namespace std;

int a[1010];

int main()
{
	int T;
	scanf("%d", &T);
	for (int tt=1; tt<=T; ++tt)
	{
		int n, maxnum=0;
		scanf("%d", &n);
		for (int i=0; i<n; ++i)
		{
			scanf("%d", a+i);
			if (a[i]>maxnum) maxnum=a[i];
		}
		int ans=maxnum;
		for (int k=1; k<maxnum; ++k)
		{
			int cnt=0;
			for (int i=0; i<n; ++i)
				if (a[i]>k) cnt+=(a[i]-k-1)/k+1;
			ans=min(ans, cnt+k);
		}
		printf("Case #%d: %d\n", tt, ans);
	}
	return 0;
}

