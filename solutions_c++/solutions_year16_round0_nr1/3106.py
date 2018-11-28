#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
	ll t,n,j;
	scanf("%lld",&t);
	j = t;
	while(t--)
	{
		scanf("%lld",&n);
		ll flag = 0,i = 0;
		ll tmp = n,tmp1;
		if(n == 0)
		{
			printf("Case #%lld: INSOMNIA\n",j-t);
		}
		else
		{
			while(flag < 1023)
			{
				tmp1 = (++i) * tmp;
				while(tmp1 > 0)
				{
					flag = flag | (1<<(tmp1%10));
					tmp1 = tmp1 / 10;
				}
			}
			printf("Case #%lld: %lld\n",j-t,i*tmp);
		}
	}
	return 0;
}
