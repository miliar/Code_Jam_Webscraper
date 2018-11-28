#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <cstdlib>
#include <string>
#include <sstream>
using namespace std;

typedef long long LL;
#define sqr(x) ((x)*(x))
#define lowbit(x) ((x)&(-x))

#define MAXN 50
#define MAXM 50

/*struct node
{
	int c, head[MAXN], to[MAXM], next[MAXM];
	void init()
	{
		c = 0;
		memset(head, -1, sizeof(head));
	}
	void add_edge(int x, int y) {
		to[c] = y;
		next[c] = head[x];
		head[x] = c++;
	}
} graph;  
*/

int n, m;

char s[MAXM][MAXM];
int ans, num;
vector<int> tong[MAXN];
set<string> myset;

void check()
{
	for (int i = 0; i < n; ++i)
		if (tong[i].size() == 0) return;
	int tmp = 0;
	for (int i = 0; i < n; ++i)
	{
		int si = tong[i].size();
		myset.clear();
		for (int j = 0; j < si; ++j)
		{
			string tmp = "";
//			cout << tong[i][j] << endl;
			int len = strlen(s[tong[i][j]]);
			for (int k = 0; k < len; ++k)
			{
				tmp = tmp + s[tong[i][j]][k];
				myset.insert(tmp);
			}
		}
		tmp += myset.size() + 1;
	}

//	cout << tmp << endl;
	if (tmp > ans)
	{
		ans = tmp; num = 1;
	}
	else if (tmp == ans) ++num;
}

void dfs(int k)
{
	if (k >= m)
	{
		check();
		return;
	}
	for (int i = 0; i < n; ++i)
	{
		tong[i].push_back(k);
		dfs(k + 1);
		tong[i].pop_back();
	}
}

int main() 
{
	int T, cases = 0;
	scanf("%d", &T);
	while (T--)
	{
		printf("Case #%d: ", ++cases);
//		printf("Case #%d:\n", ++cases);
		scanf("%d%d", &m, &n);
		for (int i = 0; i < m; ++i)
			scanf("%s", s[i]);
		for (int i = 0; i < n; ++i)
			tong[i].clear();
		ans = 0;
		num = 0;
		dfs(0);
		printf("%d %d\n", ans, num);
	}
	return 0;
}

