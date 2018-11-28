#include <cstdio>
#include <iostream>
#define ll long long
using namespace std;

int check(ll *setbits)
{
	ll i;
	for(i = 0; i < 10; i++)
	{
		if(setbits[i] == 0)
			return 1;
	}
	return 0;
}

int main()
{
	
	ll T, N, n, _N, k, gt, it;
	freopen("PA2.in", "r", stdin);
	freopen("PA2.out", "w", stdout);
	scanf("%lld", &T);
	for(it = 1; it <= T; it++)
	{
		ll setbits[10] = {0};
		scanf("%lld", &N);
		if(N == 0){
			printf("Case #%lld: INSOMNIA\n", it); continue;
		}
		_N = N;
		k = 2;
		while(check(setbits))
		{
			n = _N;
			do 
			{
			    gt = n % 10;
			    setbits[gt] = 1;
				//printf("%lld is set to 1\n", gt);
				
			    n /= 10;
			}while (n > 0);
			_N = k*N;
			k++;
		}
		_N = (k-2) * N;
		printf("Case #%lld: %lld\n", it, _N);
	}
}
