/*************************************************************************
    > File Name: GCJ_B.cpp
    > Author: ALex
    > Mail: zchao1995@gmail.com 
    > Created Time: 2015年04月11日 星期六 17时52分34秒
 ************************************************************************/

#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <stack>
#include <map>
#include <bitset>
#include <set>
#include <vector>

using namespace std;

const double pi = acos(-1.0);
const int inf = 0x3f3f3f3f;
const double eps = 1e-15;
typedef long long LL;
typedef pair <int, int> PLL;

static const int N = 1100;
int p[N];

int main()
{
//	freopen("B-large.in", "r", stdin);
//	freopen("out.out", "w", stdout);
	int t;
	int icase = 1;
	scanf("%d", &t);
	while (t--)
	{
		int n;
		scanf("%d", &n);
		int ans = inf;
		int h = 0;
		for (int i = 1; i <= n; ++i)
		{
			scanf("%d", &p[i]);
			h = max(h, p[i]);
		}
		for (int i = h; i >= 1; --i)
		{
			int tmp = i;
			for (int j = 1; j <= n; ++j)
			{
				if (p[j] > i)
				{
					tmp += p[j] / i + (p[j] % i ? 1 : 0) - 1;
				}
			}
			ans = min(ans, tmp);
		}
		printf("Case #%d: %d\n", icase++, ans);
	}
	return 0;
}
