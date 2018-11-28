#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <map>
#define clr(a,b)	memset(a,b,sizeof(a))
using namespace std;

typedef long long LL;

int T;
int d, p[1111];

bool check(int t)
{
	for(int x=1; x<=t-1; x++)
	{
		int y = t - x;

		int tot = 0;
		bool ok = true;
		for(int i=1; i<=d; i++)
		{
			int r = p[i] % y;
			if(r == 0)	tot += (p[i] / y - 1);
			else	tot += p[i] / y;

			if(tot > x)
			{
				ok = false;
				break;
			}
		}
		if(ok)
			return true;
	}
	return false;
}

int main()
{
	freopen("B-large.in","r", stdin);
	freopen("out", "w", stdout);

	int cas = 1;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&d);
		for(int i=1; i<=d; i++)
			scanf("%d", &p[i]);

		int ans = p[1];
		for(int i=2; i<=d; i++)
			ans = max(ans, p[i]);

		int l = 1, r = ans;
		while(l + 1 < r)
		{
			int mid = (l + r) >> 1;
			if(check(mid))	r = mid;
			else	l = mid;
		}
		if(check(l)) ans = l;
		else	ans = r;

		printf("Case #%d: %d\n", cas++, ans);
	}
    return 0;
}
