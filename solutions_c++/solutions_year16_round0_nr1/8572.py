#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
	ll t, ret, N, tc, temp, last, cnt, present_number, rem;
	scanf("%lld", &t);

	for(tc = 1;tc <= t;++tc)
	{
		scanf("%lld", &N);

		temp = cnt = 0;
		last = (1 << 10) - 1;

		if(N == 0)
		{
			printf("Case #%lld: INSOMNIA\n", tc);
			continue;
		}
		else
		{

			while(true)
			{
				ret = cnt*N;
				
				if(temp == last)
					break;

				++cnt;
				present_number = cnt * N;
				while(present_number > 0)
				{
					rem = present_number % 10;
					present_number /= 10;
					temp |= (1 << rem);
				}

				ret = cnt*N;
			}
		}

		printf("Case #%lld: %lld\n", tc, ret);
		
	}

	return 0;
}