#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;
const int N = 1012;
int T,ans,n,mm;
int a[N];
int main()
{
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d",&T);
	for(int t = 1;t <= T; ++ t)
	{
		scanf("%d",&n);
		ans = 0;
		for(int i = 1;i <= n;++ i)
			scanf("%d",&a[i]),ans = max(ans,a[i]);
		mm = ans;
		for(int num = 1;num <= mm; ++ num)
		{
			int tmp = 0;
			for(int i = 1;i <= n; ++ i)
				if (a[i] > num)
					tmp += ((a[i] + num - 1) / num) - 1;
			ans = min(ans,num + tmp);
		}
		printf("Case #%d: %d\n",t,ans);
	}
}