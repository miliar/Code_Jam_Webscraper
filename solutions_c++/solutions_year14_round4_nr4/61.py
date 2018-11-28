#include <cstdio>
#include <vector>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cstdlib>
using namespace std;
#define N 1001
int ans, num;
int n, m;
int a[N] = {0};
char s[N][N];
int trie[1001][50];
int calc()
{
	int tmp = 0;
	for (int i = 0; i < n; i++)
		tmp |= (1<<a[i]);
	if (tmp != (1<<m)-1)
		return 0;
	int ret = 0;
	for (int i = 0; i < m; i++)
	{
		int vnow = 1;
		for (int ll = 0; ll <= 30; ll++)
			trie[1][ll] = 0;
		
		for (int j = 0; j < n; j++)
			if (a[j] == i)
			{
				int vi = 1, k = 0;
				while (s[j][k])
				{
					if (!trie[vi][s[j][k]-'A'])
					{
						vnow++;
						trie[vi][s[j][k]-'A'] = vnow;
						memset(trie[vnow],0,sizeof trie[vnow]);
					}
					vi = trie[vi][s[j][k]-'A'];
					k++;
				}
			}
		ret += vnow;
	}
	return ret;
}

void zdfs(int vi)
{
	if (vi == n) 
	{
		int vans = calc();
		if (vans == ans)
			num++;
		else if (vans > ans)
		{
			num = 1;
			ans = vans;
		}
	} else
		for (int i = 0; i < m; i++)
		{
			a[vi] = i;
			zdfs(vi + 1);
		}
}

int main()
{
	int tot;
	freopen("d.in", "r", stdin);
	freopen("d.out", "w", stdout);
	scanf("%d", &tot);
	for (int tt = 1; tt <= tot; tt++)
	{
		
		ans = num = 0;
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++)
			scanf("%s", s[i]);
		zdfs(0);
		printf("Case #%d: ", tt);
		printf("%d %d\n", ans, num);
	}
	return 0;
}
