#include <cstdio>
#include <cstring>
#include <algorithm>
#define fo(i,a,b) for (int i = a;i <= b;i ++)

int T,cas,N;
bool f[10];

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	for (scanf("%d",&T);T;T --)
	{
		printf("Case #%d: ",++cas);
		scanf("%d",&N);
		memset(f,0,sizeof f);
		if (N == 0)
		{
			puts("INSOMNIA");
			continue;
		}
		fo(i,1,100)
		{
			int x = N * i;
			while (x > 0)
			{
				f[x%10] = 1;
				x /= 10;
			}
			bool ok = 1;
			fo(j,0,9) if (!f[j]) ok = 0;
			if (ok)
			{
				printf("%d\n",N*i);
				break;
			}
		}
	}
	return 0;
}
