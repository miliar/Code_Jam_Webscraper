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

#define MAXN 10005
#define MAXM 1000

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
int a[MAXN];

int main() 
{
	int T, cases = 0;
	scanf("%d", &T);
	while (T--)
	{
		printf("Case #%d: ", ++cases);
//		printf("Case #%d:\n", ++cases);
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i)
			scanf("%d", &a[i]);
		sort(a, a + n);
		int i = 0, j = n - 1;
		int ans = 0;
		while (i <= j)
		{
			if (i == j) 
			{
				++ans;
				break;
			}
			if (a[i] + a[j] <= m)
			{
				++ans;
				++i;
				--j;
			}
			else
			{
				++ans;
				--j;
			}
//			cout << i << ' ' << j << ' ' << ans << endl;
		}
		printf("%d\n", ans);
	}
	return 0;
}
