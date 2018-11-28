/*
* @problem: Counting Sheep
*/

#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <limits.h>
#include <vector>
#include <map>
#include <bitset>
#include <string>
#include <iterator>
#include <set>
#include <utility>
#include <queue>
#include <numeric>
#include <functional>
#include <ctype.h>
#include <stack>
#include <algorithm>
#include <cstdlib>
#define MAX 100100
#define mod 1000000007LL
#define bitcnt(x) __builtin_popcount(x)
#define MS0(x) memset(x, 0, sizeof(x))
#define MS1(x) memset(x, -1, sizeof(x))
#define ll long long int
#define pii pair<int, int>
#define pll pair<long long int,long long int>
#define in(x) scanf("%lld", &x)
#define ind(x) scanf("%d", &x)
#define ins(x) scanf("%s", x)
#define pi acos(-1.0)

using namespace std;

int main()
{
	// ios_base::sync_with_stdio(0);
    // cin.tie(0);
	int t;
	ll mask, tmp, tmp1, ans, n, c = (1 << 10) - 1;
	int x;
	ind(t);
	for(int i = 1; i <= t; i++)
	{
		in(n);
		if(n == 0)
		{
			printf("Case #%d: INSOMNIA\n", i);
			continue;
		}
		tmp1 = n;
		ans = 0;
		mask = 0;
		while(mask != c)
		{
			tmp = n;
			while(tmp > 0)
			{
				x = tmp % 10;
				tmp /= 10;
				mask = mask | (1LL << x);
			}
			if(mask == c)
			{
				ans = n;
				break;
			}
			n += tmp1;
		}
		printf("Case #%d: %lld\n", i, ans);
	}
	return 0;
}