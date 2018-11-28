#include<bits/stdc++.h>
#define ll long long
using namespace std;
ll isPrime(ll a)
{
	ll i;
	for(i = 3 ; i*i <= a ; i += 2 )
	{
		if( a%i == 0 )
		{
			return i;
		}
	}
	return -1;	
}
ll power(ll a,ll b)
{
	ll ans = 1,tmp = a;
	while(b > 0)
	{
		if(b&1)
		{
			ans *= tmp;
		}
		tmp = tmp * tmp;
		b = b>>1;
	}
	return ans;
}
int main()
{
	ll n,j,t;
	scanf("%lld",&t);
	ll tmp = t;
	while(t--)
	{
		scanf("%lld%lld",&n,&j);
		printf("Case #%lld:\n", tmp - t);
		ll r;
		j = 0;
		for(r = 0 ; r <= 16383 && j < 50 ; r++ )
		{
			ll no = r<<1 | 1 | 1<<15 ;
			ll bases[11],base;
			for(base = 2; base <= 10 ; base++ )
			{
				ll a = 0, tmp1 = 15;
				for(ll i = 1<<15 ; i > 0 ; i>>=1, tmp1-- )
				{
					if( no & i )
					{
						//a += base^log2(i);
						a += power( base, tmp1 );
					}
				}
				ll primality = isPrime(a);
				if(primality > 0)
				{
					bases[base] = primality;
				}
				else
					break;
			}
			if(base == 11)
			{
				j++;
				for( ll i = 1<<15 ; i > 0 ; i>>=1 )
				{
					if(no & i)
					{
						printf("1");
					}
					else
						printf("0");
				}
				printf(" ");
				for(ll i = 2 ; i <= 10 ; i++ )
				{
					printf("%lld ",bases[i]);
				}
				printf("\n");
			}
		}
	}
	return 0;
}
