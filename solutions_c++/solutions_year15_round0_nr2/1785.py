#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>
#include <set>

using namespace std;

int a[2000], n;

int f[2000][2000];

int main()
{
	int T;
	scanf("%d", &T);
	for(int cas = 1; cas <= T; ++cas)
	{
		scanf("%d", &n);
		for(int i = 0; i < n; ++i)
			scanf("%d", &a[i]);
		sort(a, a + n);
		int ans = 0x3f3f3f3f;
		for(int mxval = 1; mxval <= a[n - 1]; ++mxval)
		{
			int totTime = 0;
			for(int j = 0; j < n; ++j)
			{
				if(a[j] > mxval)
				{
					totTime += a[j] / mxval;
					if(a[j] % mxval == 0) totTime -= 1;
				}
			}
			ans = min(ans, totTime + mxval);
		}
		printf("Case #%d: %d\n", cas, ans);
	}
	return 0;
}
