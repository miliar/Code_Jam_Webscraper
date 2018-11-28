#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <string>
#define lld long long
#define INF 2100000000
#define eps 1e-8
#define mem(a,b) memset(a,b,sizeof(a))

using namespace std;
struct nod
{
	int ch[26];
	int p;
	int sum;
};
char str[200][200];
struct trie
{
	int tot;
	nod node[2000];
	int root;

	void init()
	{
		tot = 0;
		root = newnode();
	}
	int newnode()
	{
		tot++;
		mem(node[tot].ch, -1);
		node[tot].p = tot;
		node[tot].sum = 0;
		return tot;
	}

	void ins(char * s)
	{
		int now = root;
//		cout<<s;
		while (*s)
		{
			int x = *s - 'A';

			if (node[now].ch[x] == -1)
			{
				node[now].ch[x] = newnode();
			}

			node[node[now].ch[x]].sum++;
			now = node[now].ch[x];
			s++;
		}
//		cout<<s<<"  "<<tot<<endl;
	}

	int cal(char * s)
	{
		int now = root;

		while (*s)
		{
			int x = *s - 'A';

			if (node[now].ch[x] == -1)
			{
				return 0;
			}

			now = node[now].ch[x];
			s++;
		}

		return node[now].sum;
	}
}tr[5];
int maxn, way;
int vis[200];
int n, m;
void dfs(int u, int p){
	int i, j;
	if (u == m){
		for(i = 1; i <= n; i++)
			tr[i].init();
//		for(i = 1; i <= m; i++)
//			cout<<vis[i]<<"  ";
//		cout<<endl;
		for(i = 1; i <= m; i++)
			tr[vis[i]].ins(str[i]);
		int ans = 0;
		for(i = 1; i <= n; i++){
			if (tr[i].tot != 1)
			ans += tr[i].tot;
		}
//		cout<<ans<<endl;
		if (ans > maxn){
			way = 1;
			maxn = ans;
		} else if (ans == maxn) way++;
		return ;
	}
	for(i = 1; i <= n; i++){
		vis[u + 1] = i;
		dfs(u + 1, i);
	}
}

int main()
{
	int T;
	int i, j, cas = 0;
//
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	cin >> T;

	while (T--)
	{
		scanf("%d%d", &m, &n);
		way = 0;
		maxn = 0;
		for(i = 1; i <= m; i++)
			scanf("%s", str[i]);
		mem(vis, 0);
		for(i = 1; i <= n; i++){
			vis[1] = i;
			dfs(1, i);
		}
		printf("Case #%d: %d %d\n", ++cas, maxn, way);
	}

	return 0;
}
