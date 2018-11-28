/*************************************************************************
    > File Name: GCJ_A.cpp
    > Author: ALex
    > Mail: zchao1995@gmail.com 
    > Created Time: 2015年04月11日 星期六 16时56分27秒
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

static const int N = 1200;
char str[N];

int main()
{
	int n, t;
//	freopen("A-large.in", "r", stdin);
//	freopen("A.out", "w", stdout);
	int icase = 1;
	scanf("%d", &t);
	while (t--)
	{
		scanf("%d%s", &n, str);
		int ans = 0;
		int sum = str[0] - '0';
		for (int i = 1; i <= n; ++i)
		{
			if (str[i] != '0' && sum < i)
			{
				ans += i - sum;
				sum += str[i] - '0' + i - sum;
			}
			else
			{
				sum += str[i] - '0';
			}
		}
		printf("Case #%d: %d\n", icase++, ans);
	}
	return 0;
}
