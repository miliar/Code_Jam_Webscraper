#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int n, m;
int s[1000];
int prime[1100000], p1[1100000], p2[1100000];
int p[1100000];
int cnt;
void init()
{
	int i, j; cnt = 0; int v1, v2, tot; int tt = 0;
	for (i = 2; 2 * i <= 1000010; i++) if (!p[i])
	for (j = 2 * i; j<1000010; j += i)
		p[j] = i;
	for (i = 2, cnt = 0; i<1000010; ++i) if (!p[i])
		prime[cnt++] = i;
}
int check(long long x)
{
	for (int i = 0; i < cnt; i++)
	{
		if (x<prime[i])
			break;
		if (x%prime[i] == 0 && x!=prime[i])
			return prime[i];
	}
	return 0;
}
int ans[1000];
int main()
{
	int ncase, i, j, tt = 0;
	
	init();
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	scanf("%d", &ncase);
	while (ncase--)
	{
		scanf("%d %d", &n, &m);
		printf("Case #%d:\n", ++tt);
		int aa = 0;
		for (i = 0; i<(1 << (n - 2)); i++)
		{
			s[0] = 1;
			int j = 1, x = i;
			while (x)
			{
				s[j++] = x % 2;
				x /= 2;
			}
			for (int q = j - 1; q<(n - 2); q++)
			{
				s[j++] = 0;
			}
			s[j] = 1;

			int tot = 0;
			int flag = 0;
			for (int q = 2; q <= 10; q++)
			{
				long long y = 0;
				for (int k = n-1; k>=0; k--)
					y = y*q + (s[k]);
				int tx = check(y);
				if (!tx){
					flag = 1;
					break;
				}
				ans[tot++] = tx;
			}
			if (!flag)
			{
				aa++;
				for (int k = j; k >= 0; k--)
					printf("%d", s[k]);
				printf(" ");
				for (int k = 0; k<tot; k++)
				{
					if (k == tot - 1)
						printf("%d\n", ans[k]);
					else
						printf("%d ", ans[k]);
				}
				if (aa == m)
					break;
			}
		}
	}
	return 0;
}
