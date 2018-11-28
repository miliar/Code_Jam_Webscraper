#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>

using namespace std;
const int N = 112;
int T,n,m,k,tmp,ans;
bool f[N][N];
int main()
{
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d",&T);
	for(int t = 1;t <= T; ++ t)
	{
		scanf("%d%d%d",&n,&m,&k);
		ans = n * m;
		for(int i = 1;i <= k; ++ i)
		{
			memset(f,0,sizeof(f));
			for(int i1 = 1;i1 <= n;++ i1)
			{
				int o = (i + i1 - 2) % k + 1;
				while (o <= m)
					f[i1][o] = true,o += k;
			}
			tmp = 0;
			for(int i1 = 1;i1 <= m; ++ i1)
				if (f[n][i1]) tmp = i1;
			if (tmp == m) 
			{
				if (n >= k)
					tmp = k;
				else
					tmp = k - 1;
			}
			else 
			{
				if (n >= k)
					tmp = k + 1;
				else
					tmp = k;
			}
			for(int i1 = 1;i1 <= n; ++ i1)
			for(int j1 = 1;j1 <= m; ++ j1)
				tmp += f[i1][j1];
			ans = min(ans,tmp);
		}
		for(int i = 1;i <= k; ++ i)
		{
			memset(f,0,sizeof(f));
			for(int i1 = 1;i1 <= m;++ i1)
			{
				int o = (i + i1 - 2) % k + 1;
				while (o <= n)
					f[o][i1] = true,o += k;
			}
			tmp = 0;
			tmp = 0;
			for(int i1 = 1;i1 <= n; ++ i1)
				if (f[i1][m]) tmp = i1;
			if (tmp == n) 
			{
				if (m >= k)
					tmp = k;
				else
					tmp = k - 1;
			}
			else 
			{
				if (m >= k)
					tmp = k + 1;
				else
					tmp = k;
			}
			for(int i1 = 1;i1 <= n; ++ i1)
			for(int j1 = 1;j1 <= m; ++ j1)
				tmp += f[i1][j1];
			ans = min(ans,tmp);
		}
		printf("Case #%d: %d\n",t,ans);
	}
}