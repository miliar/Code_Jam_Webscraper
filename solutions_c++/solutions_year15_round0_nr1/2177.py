#define _CRT_SECURE_NO_WARNINGS
#pragma comment (linker,"/STACK:256000000")
#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<deque>
#include<vector>
#include<cassert>
#include<string>
using namespace std;

#define INF 1000000000
#define lint long long
#define pb push_back
#define mp make_pair
#define MOD 1000000007

int d[1005];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tc, T = 0;
	scanf("%d", &tc);
	while(tc--)
	{
		int n, i;
		char s[1005];
		scanf("%d %s", &n, s);
		for (i = 0; i <= n; ++i)
		{
			d[i] = s[i] - '0';
		}

		int ans = 0, cnt = 0;
		for (i = 0; i <= n; ++i)
		{
			if (!d[i]) continue;
			if (i > cnt)
			{
				ans += i - cnt;
				cnt = i + d[i];
			}
			else
				cnt += d[i];
		}

		printf("Case #%d: %d\n", ++T, ans);
	}
	return 0;
}
