#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

ll solve(ll n)
{
	bool was[10]={0};
	bool f=1;
	ll nc=n;
	int cnt=1;
	do
	{
		while(n>0)
		{
			if(n) was[n%10]=1;
			n/=10;
		}
		if(n<0) cerr<<"!!!!!\n";
		n=nc*(++cnt);
		f=0;
		for(int i=0;i<10;i++)
			if(!was[i]) f=1;
	} while(f);
	return nc*(cnt-1);
}

int main()
{
	int t;
	ll n;
	scanf("%d", &t);
	for(int tc=1;tc<=t;tc++)
	{
		scanf("%Ld", &n);
		if(n)
			printf("Case #%d: %Ld\n", tc, solve(n));
		else
			printf("Case #%d: INSOMNIA\n", tc);
	}
	return 0;
}