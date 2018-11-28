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

#define MAXN 1005
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
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf("%d", &a[i]);
		int l = 0, r = n - 1;
		int ans = 0;
		while (l < r)
		{
			int mini = l;
			for (int i = l + 1; i <= r; ++i)
			{
				if (a[mini] > a[i]) mini = i;
			}
			//left
			if (mini - l <= r - mini)
			{
				for (int i = mini; i > l; --i)
				{
					a[i] = a[i - 1];
					++ans;
				}
				++l;
			}
			else // right
			{
				for (int i = mini; i < r; ++i)
				{
					a[i] = a[i + 1];
					++ans;
				}
				--r;
			}
		}
		printf("%d\n", ans);
	}
	return 0;
}

