#include<bits/stdc++.h>
#define ll long long int
#define pb push_back
#define MOD 1000000007
using namespace std;

ll p[11][16],v[16],d[11];
ll co=0;

ll prime(ll n)
{
	if(n%2==0)
	return 2;
	for(ll i=3;i*i<=n;i+=2)
	{
		if(n%i==0)
		return i;
	}
	return 0;
}

void fun(ll cur)
{
	if(co<50)
	{
		if(cur==15)
		{
			ll flag=0;
			for(ll i=2;i<11;++i)
			{
				d[i]=0;
				for(ll j=0;j<16;++j)
				d[i]=d[i]+v[j]*p[i][j];
				ll temp=prime(d[i]);
				if(temp==0)
				{
					flag=1;
					break;
				}
				else
				d[i]=temp;
			}
			if(!flag)
			{
				for(ll i=15;i>=0;--i)
				printf("%lld",v[i]);
				printf(" ");
				for(ll i=2;i<11;++i)
				printf("%lld ",d[i]);
				printf("\n");
				co++;
			}
		}
		else
		{
			v[cur]=1;
			fun(cur+1);
			v[cur]=0;
			fun(cur+1);
		}	
	}	
}

int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("out5.out","w",stdout);
	for(ll i=2;i<11;++i)
	{
		p[i][0]=1;
		for(ll j=1;j<16;++j)
		p[i][j]=p[i][j-1]*i;
	}
	ll t,n,j,x;
	scanf("%lld",&t);
	for(ll x=1;x<=t;++x)
	{
		scanf("%lld%lld",&n,&j);
		printf("Case #1:\n");
		v[0]=1;
		v[15]=1;
		fun(1);
	}
	return 0;
}
