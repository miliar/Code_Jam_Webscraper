/*    SHUBHAM SINHA    */



#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <math.h>

#define ll long long int
#define maxN 1000000
#define maxVal 100000000
#define minVal -100000000
#define mod 1000000007LL

#define gcd(a,b) __gcd(a,b)

using namespace std;

int n,j,c;

ll power(ll a,ll b)
{
	ll x=1,y=a;
	while(b>0)
	{
		if(b%2==1)
			x=(x*y);
		y=(y*y);
		b=b/2;
	}
	return x;
}

ll convert2(ll a)
{
	ll r=0,x,k=0;
	while(a>0)
	{
		x=a%10;
		if(x)
			r=r+power(2,k);
		k++;
		a=a/10;
	}
	return r;
}

ll convert3(ll a)
{
	ll r=0,x,k=0;
	while(a>0)
	{
		x=a%10;
		if(x)
			r=r+power(3,k);
		k++;
		a=a/10;
	}
	return r;
}

ll convert4(ll a)
{
	ll r=0,x,k=0;
	while(a>0)
	{
		x=a%10;
		if(x)
			r=r+power(4,k);
		k++;
		a=a/10;
	}
	return r;
}

ll convert5(ll a)
{
	ll r=0,x,k=0;
	while(a>0)
	{
		x=a%10;
		if(x)
			r=r+power(5,k);
		k++;
		a=a/10;
	}
	return r;
}

ll convert6(ll a)
{
	ll r=0,x,k=0;
	while(a>0)
	{
		x=a%10;
		if(x)
			r=r+power(6,k);
		k++;
		a=a/10;
	}
	return r;
}

ll convert7(ll a)
{
	ll r=0,x,k=0;
	while(a>0)
	{
		x=a%10;
		if(x)
			r=r+power(7,k);
		k++;
		a=a/10;
	}
	return r;
}

ll convert8(ll a)
{
	ll r=0,x,k=0;
	while(a>0)
	{
		x=a%10;
		if(x)
			r=r+power(8,k);
		k++;
		a=a/10;
	}
	return r;
}

ll convert9(ll a)
{
	ll r=0,x,k=0;
	while(a>0)
	{
		x=a%10;
		if(x)
			r=r+power(9,k);
		k++;
		a=a/10;
	}
	return r;
}

ll convert10(ll a)
{
	return a;
}

ll prime(ll a)
{
	ll i;
	for(i=2;i<=sqrt(a);i++)
	{
		if(a%i==0)
			return i;
	}
	return -1;
}

void compute(int i,ll a)
{
	if(c>=j)
		return;
	if(i==n)
	{
		ll a2,a3,a4,a5,a6,a7,a8,a9,a10;
		ll m2,m3,m4,m5,m6,m7,m8,m9,m10;
		a2=convert2(a);
		m2=prime(a2);
		if(m2==-1)
			return;
		a3=convert3(a);
		m3=prime(a3);
		if(m3==-1)
			return;
		a4=convert4(a);
		m4=prime(a4);
		if(m4==-1)
			return;
		a5=convert5(a);
		m5=prime(a5);
		if(m5==-1)
			return;
		a6=convert6(a);
		m6=prime(a6);
		if(m6==-1)
			return;
		a7=convert7(a);
		m7=prime(a7);
		if(m7==-1)
			return;
		a8=convert8(a);
		m8=prime(a8);
		if(m8==-1)
			return;
		a9=convert9(a);
		m9=prime(a9);
		if(m9==-1)
			return;
		a10=convert10(a);
		m10=prime(a10);
		if(m10==-1)
			return;
		printf("%lld ",a);
		printf("%lld %lld %lld %lld %lld %lld %lld %lld %lld\n",
				m2,m3,m4,m5,m6,m7,m8,m9,m10);
		c++;
		return;
	}
	if(i==0||i==n-1)
		compute(i+1,a*10+1);
	else
	{
		compute(i+1,a*10+0);
		compute(i+1,a*10+1);
	}
}

int main()
{
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    #ifndef LOCAL_SYS
        freopen("C-small-attempt0.in","r",stdin);
        freopen("out.txt","w",stdout);
    #endif
    int t;
    scanf("%d",&t);
    while(true)
    {
    	scanf("%d%d",&n,&j);
    	printf("Case #%d:\n",t);
    	c=0;
    	compute(0,0);
    	break;
    }
    return 0;
}