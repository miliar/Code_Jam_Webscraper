#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int T;
	long long r, t;
	scanf("%d", &T);
	for(int x=1; x<=T; ++x)
	{
		scanf("%lld%lld", &r, &t);
		long long low, high, n;
		double v;
		long long ans = 1;
		low = 1;
		high = t;
		while(low < high)
		{
			n = (low + high) / 2;
			v = 2.0*n*n + 2.0*r*n - n;
			if(v > t)
			{
				high = n;
			}
			else if(v < t)
			{
			    ans = n;
				low = n + 1;
			}
			else
			{
				ans = n;
				break;
			}
		}
		
		printf("Case #%d: %lld\n", x, ans);
	}
	
	return 0;
}
