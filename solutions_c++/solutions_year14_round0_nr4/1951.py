#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;
const int N = 1012;
int T,n,ans2,ans1,num,now;
double a[N],b[N];
bool flag,f[N];
int main()
{
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d",&T);
	for(int t = 1; t <= T; ++ t)
	{
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		scanf("%d",&n);
		for(int i = 1; i <= n;++ i)
			scanf("%lf",&a[i]);
		for(int i = 1; i <= n;++ i)
			scanf("%lf",&b[i]);
		sort(a + 1, a + n + 1);
		sort(b + 1, b + n + 1);
		memset(f,0,sizeof(f));
		ans2 = 0;
		for(int i = 1; i <= n; ++ i)
		{
			flag = false;
			for(int j = 1; j <= n; ++ j)
				if (!f[j] && b[j] > a[i])
				{
					f[j] = true;
					flag = true;
					break;
				}
			if (!flag)
			for(int j = 1; j <= n; ++ j)
			if (!f[j])
			{
				++ans2;
				break;
			}
		}
		ans1 = 0;
		for(int i = 0; i <= n; ++ i)
		{
			flag = false;
			num = i;
			now = i;
			for(int j = 1; j <= n; ++ j)
			{
				++now;
				//printf("%d %d %d %d \n",i,j,num,now);
				if (now > n) break;
				if (b[j] >= a[now])
				{
					--num;
					--now;
					if (num < 0)
					{
						flag = true;
						break;
					}
				}
			}
			if (!flag)
			{
				ans1 = n - i;
				break;
			}
		}
		printf("Case #%d: %d %d\n",t,ans1,ans2);
	}
}