#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>
using namespace std;

long long gcd_iter(long long u, long long v);
bool isPower2(long long a,long long & res);
long long numShifts(long long a);
long long computeShifts(long long num , long long denom);

int main()
{
	long long t,i;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cout<<"Case #"<<i<<": ";
		long long numerator,denominator;
		scanf("%lld/%lld",&numerator,&denominator);
		long long gcd= gcd_iter(numerator,denominator);
		numerator = numerator/gcd;
		denominator = denominator/gcd;
		long long res=0;
		if(numerator ==1 && denominator ==1)
		{cout<<0<<endl;}
		else
		{
			if(isPower2(denominator,res))
			{
				/*//if(numerator>1)
				//{
					long long n=numShifts(numerator);
					res = res - n;
				//}*/
				res = computeShifts(numerator,denominator);
				cout<<res<<endl;
			}
			else
			{
				cout<<"impossible"<<endl;
			}
		}
	}
}

long long gcd_iter(long long u, long long v)
{
	long long t;
	while (v)
	{
		t = u; 
		u = v; 
		v = t % v;
	}
	return u < 0 ? -u : u; /* abs(u) */
}

bool isPower2(long long a,long long & res)
{
	res=0;
	bool ret = true;
	while(a>1)
	{
		if(a&1 == 1)
		{
			ret = false;
			break;
		}
		a=a>>1;
		res++;
	}
	return ret;
}

long long numShifts(long long a)
{
	long long ret =0,t;
	while(a>1)
	{
		if(isPower2(a,t))
		{break;}
		ret++;
		a=a>>1;
	}
	return ret;
}


long long computeShifts(long long num , long long denom)
{
	long long ret = 0 ;
	while(denom>num)
	{
		ret++;
		denom = denom>>1;
	}
	return ret;
}
