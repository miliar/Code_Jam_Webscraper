#include <bits/stdc++.h>

using namespace std;

int extract(int x)
{
	int ret = 0;
	while (x)
	{	
		ret |= (1 << (x%10));
		x/=10;
	}
	return ret;
}

int main()
{
	int T, casecnt = 0;
	scanf("%d", &T);
	while(T--)
	{
		int n;
		scanf("%d", &n);
		if (n == 0)
		{
			printf("Case #%d: INSOMNIA\n", ++casecnt);
			continue;
		}
		int k = 0, mask = 0;
		while (mask != (1 << 10)-1)
		{
			k++;
			mask |= extract(k*n);
		}
		printf("Case #%d: %d\n", ++casecnt, k*n);
	}
	return 0;
}
