#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main()
{
    freopen("A-large.in","r",stdin);
    freopen("dataA.out","w",stdout);
	const int ed = 1023;
	int T, ys = 0;
	scanf("%d", &T);
	while (T--)
	{
		long long x, a;
		scanf("%lld", &a);
		printf("Case #%d: ", ++ys);
		x = a;
		if (x == 0)
		{
			printf("INSOMNIA\n");
			continue;
		}
		int st = 0;
		while (x < 1000000000000000LL)
		{
			long long t = x;
			while (t)
			{
				int d = t % 10;
				t /= 10;
				st |= (1 << d);
			}
			if (st == ed) break;
			x += a;
		}
		printf("%lld\n", x);
	}

	return 0;
}