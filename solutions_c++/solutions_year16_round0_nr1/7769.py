#include <bits/stdc++.h>

using namespace std;

#define ll long long

bool flag[10];

ll calc(ll a)
{
	int digits_seen = 0;
	for(int j=0;j<10;j++)
		flag[j] = false;
	int result = 0;
	ll t=a;
	for(;digits_seen<10;t+=a)
	{
		ll temp = t;
		while(temp>0)
		{
			if(!flag[temp%10])
			{
				digits_seen++;
				flag[temp%10] = true;
			}
			temp/=10;
		}
	        
	}
	return (t-a);
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int i=1;i<=T;i++)
	{
		ll a;
		scanf("%lld", &a);
		if(a==0)
			printf("Case #%d: INSOMNIA\n", i);
		else
			printf("Case #%d: %lld\n", i, calc(a));
	}

}
