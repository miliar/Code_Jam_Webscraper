#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
using namespace std;
int _, __;
int n, cnt;
char ty[20];
int id[20];
int vis[101000], pis[101000];
map<int, int> mp;
int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	for (scanf("%d", &_); _; _--)
	{
		scanf("%d ", &n);
		mp.clear();
		cnt = 0;
		for (int i = 0; i < n; i++)
		{
			scanf("%c %d ", ty + i, id + i);
			--id[i];
			if (id[i] == -1) continue;
			if (!mp.count(id[i])) mp[id[i]] = cnt++;
			id[i] = mp[id[i]];
		}
		for (int S = 0; S < (1 << n); S++) vis[S] = 1;
		for (int i = 0; i < n; i++)
		{
			for (int S = 0; S < (1 << n); S++) pis[S] = vis[S], vis[S] = 0;
			for (int S = 0; S < (1 << n); S++) if (pis[S])
				{
					if (ty[i] == 'E')
					{
						if (id[i] != -1)
						{
							if (!(S & (1 << id[i]))) vis[S ^ (1 << id[i])] = 1;
						}
						else
						{
							for (int j = 0; j < n; j++) if (!(S & (1 << j))) vis[S ^ (1 << j)] = 1;
						}
					}
					else
					{
						if (id[i] != -1)
						{
							if ((S & (1 << id[i]))) vis[S ^ (1 << id[i])] = 1;
						}
						else
						{
							for (int j = 0; j < n; j++) if ((S & (1 << j))) vis[S ^ (1 << j)] = 1;
						}
					}
				}
		}
		int ans = n + 1;
		for (int S = 0; S < (1 << n); S++) if (vis[S]) ans = min(ans, __builtin_popcount(S));
		if (ans > n) printf("Case #%d: CRIME TIME\n", ++__);
		else printf("Case #%d: %d\n", ++__, ans);
	}
}
