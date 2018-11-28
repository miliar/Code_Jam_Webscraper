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

int a[1005];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tc, T = 0;
	scanf("%d", &tc);
	while(tc--)
	{
		int n, i, j, r, c;
		scanf("%d %d %d", &n, &r, &c);
		if (r > c)
			swap(r, c);
		bool ans = 1;
		ans &= ((r*c) % n == 0);

		for (i = 1; i*i <= n; ++i)
		{
			if (n % i != 0)
				continue;
			int a = i;
			int b = n / i;

			if ((a > r || b > c) && (a > c || b > r))
				ans = 0;
		}

		if (n == 4)
		{
			if (r == 1 && c == 4)
				ans = 0;
			if (r == 2 && c == 2)
				ans = 0;
			if (r == 2 && c == 4)
				ans = 0;
		}
		if (n == 1)
			ans = 1;

		if (n == 3)
		{
			if (r == 1 && c == 3)
				ans = 0;
		}
		if (ans)
			printf("Case #%d: GABRIEL\n", ++T);
		else
			printf("Case #%d: RICHARD\n", ++T);
	}
	return 0;
}
