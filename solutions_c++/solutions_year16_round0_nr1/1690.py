#include <iostream>
#include <fstream>
#include <cstdio>
#include <climits>
#include <vector>
#include <map>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <string>
#include <cstring>
#include <algorithm>
#include <bitset>
#include <cmath>
#include <functional>

using namespace std;

#define ll long long
#define vt vector
#define mod 1000000007

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int cases = 1; cases <= t; cases++)
	{
		ll n;
		scanf("%lld", &n);
		if (n == 0)
			printf("Case #%d: INSOMNIA\n", cases);
		else
		{
			bool digits[10] = { 0 };
			ll iter = 1;
			int cnt = 0;
			while (cnt < 10 && iter < 1e8)
			{
				ll temp = n * iter;
				while (temp > 0)
				{
					if (!digits[temp % 10])
					{
						digits[temp % 10] = 1;
						cnt++;
					}
					temp /= 10;
				}
				iter++;
			}
			if (cnt == 10)
				printf("Case #%d: %lld\n", cases, n * (iter-1));
			else
				printf("Case #%d: INSOMNIA\n", cases);
		}
	}
	return 0;
}