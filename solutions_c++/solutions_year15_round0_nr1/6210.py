#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <algorithm>

typedef long long ll;
#define mp make_pair
#define mt(a, b, c) mp(a, mp(b, c))
#define ZERO(x) memset((x), 0, sizeof(x))
#define MAXN 2*10000500

using namespace std;

int main()
{
#ifdef DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int T = 0;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		int k;
		cin >> k;
		ll ans = 0;
		ll cur = 0;
		
		char c;
		cin >> c;
		cur = c - '0';

		for (int j = 1; j <= k; j++)
		{
			scanf("%c", &c);
			int r = c - '0';

			if (r > 0 && cur < j)
			{
				ans += j - cur;
				cur = j;
			}
			cur += r;
		}

		printf("Case #%d: %lld\n", i + 1, ans);
	}

	return 0;
}