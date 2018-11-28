/*
* @problem: Revenge of the Pancakes
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
	int t, ans, c, l, tmp;
	char s[105];
	ind(t);
	for(int i = 1; i <= t; i++)
	{
		ins(s);
		l = strlen(s);
		c = 0;
		ans = 0;
		for(int j = 0; j < l; j++)
		{
			if(s[j] == '-')
				c++;
		}
		while(c > 0)
		{
			int j;
			tmp = 0;
			for(j = 0; j < l && s[j] == '+'; j++)
				s[j] = '-';
			c += j;
			if(j)
				ans++;
			for(j = 0; j < l && s[j] == '-'; j++)
				s[j] = '+';
			c -= j;
			if(j)
				ans++;
		}
		printf("Case #%d: %d\n", i, ans);
	}
	return 0;
}