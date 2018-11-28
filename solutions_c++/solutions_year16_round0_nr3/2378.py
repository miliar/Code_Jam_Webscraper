#include <cstdio>
#include <cstring>
#include <algorithm>
#define fo(i,a,b) for (int i = a;i <= b;i ++)

int T,N,J,cnt;
int a[35],fac[15];

void dfs(int x)
{
	if (cnt >= J) return;
	if (x > N)
	{
		bool ok = 1;
		memset(fac,0,sizeof fac);
		fo(i,2,10)
		{
			long long p = 1, y = 0;
			fo(j,1,N)
			{
				y += p * a[j];
				p *= i;
			}
			for (long long k = 2;k * k <= y;k += 1)
				if (y % k == 0)
				{
					fac[i] = k;
					break;
				}
			if (fac[i] == 0)
			{
				ok = 0;
				break;
			}
		}
		if (ok && cnt < J)
		{
			for (int i = N;i >= 1;i --) printf("%d",a[i]);
			fo(i,2,10) printf(" %d",fac[i]);
			printf("\n");
			cnt ++;
		}
		return;
	}
	if (x == 1 || x == N)
	{
		a[x] = 1;
		dfs(x+1);
	}
	else
	{
		a[x] = 0;
		dfs(x+1);
		a[x] = 1;
		dfs(x+1);
	}
}

int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	scanf("%d",&T);
	scanf("%d%d",&N,&J);
	printf("Case #1:\n");
	dfs(1);
	return 0;
}
