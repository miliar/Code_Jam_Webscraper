#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <queue>
#define LL long long

using namespace std;

const int INF = 0x3f3f3f3f;
const int N = 1555;

int n;
char num[N];

int main()
{
//	freopen("A-large.in", "r", stdin);
//	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	int cas = 0;
	while (t--)
	{
		scanf("%d %s", &n, num);
		int i, j;
		int cur = num[0] - '0';
		int ans = 0;
		
		for (i = 1; i <= n; ++i)
		{
			if (cur < i)
			{
				
				ans += i - cur;
				cur = i;
			}
			cur += num[i] - '0';
		}
		printf("Case #%d: %d\n", ++cas, ans);
	}
}