#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int a[1005];
int n,test;

int main()
{
	//freopen("B-small-attempt0.in","r",stdin);
	freopen("B-large.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&test);
	//puts("x");
	for (int T = 1; T <= test; T++)
	{
		scanf("%d",&n);
		for (int i = 0; i < n; i++) scanf("%d",a + i);
		int ans = 0,s = 0,t = n - 1;
		//puts("x");
		while (s < t)
		{
			int k = t;
			for (int i = s; i < t; i++) if (a[i] < a[k]) k = i;
			if (k - s <= t - k)
			{
				for (int i = k - 1; i >= s; i--)
				{
					int tg = a[i + 1];
					a[i + 1] = a[i];
					a[i] = tg;
					ans++;
				}
				s++;
			} else
			{
				for (int i = k; i < t; i++)
				{
					int tg = a[i + 1];
					a[i + 1] = a[i];
					a[i] = tg;
					ans++;
				}
				t--;
			}
			//printf("%d %d:\n",s,t);
			//for (int i = 0; i < n; i++) printf("%d ",a[i]); puts("");
		}
		printf("Case #%d: %d\n",T,ans);
	}
}
