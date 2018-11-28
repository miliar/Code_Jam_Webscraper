#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long int ll;

int main()
{
	int t;
	scanf("%d", &t);
	
	for(int j=1;j<=t;j++)
	{
		ll n;

		scanf("%llu", &n);

		if(n==0)		
		{
			printf("Case #%d: INSOMNIA\n",j);
			continue;
		}
		set<int> s;
	
		ll x = n;
		ll val=n;

		while(x)
		{
			s.insert(x%10);
			x/=10;
		}
		
		ll i=2;
		while(s.size()!=10)
		{
			ll temp=n*i;
			val = temp;
				while(temp)
				{
					s.insert(temp%10);
					temp/=10;
				}
			i++;	
		}
		
		printf("Case #%d: %llu\n",j, val);
	}
}
