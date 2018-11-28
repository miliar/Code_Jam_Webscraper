#include<bits/stdc++.h>
#define ll long long int

using namespace std;

int main()
{
	ll t;
	ll sum=0;
	ll smax=0;
	ll scnt=0;
	scanf("%lld", &t);
	for(ll i=1;i<=t; i++)
	{
		scanf("%lld", &smax);
		char a[smax+1];
		sum=0;
		scnt=0;
		scanf("%s", a);
		for(ll j=0; j<=smax; j++)
		{
			//cout<<((int)a[j]-48)<<endl;
			if(j>scnt)
			{
				sum+=(j-scnt);
				scnt+=(j-scnt+(int)a[j]-48);
			}
			else
				scnt+=((int)a[j]-48);
		}
		printf("Case #%lld: %lld\n", i, sum);
	}
	return 0;
}
