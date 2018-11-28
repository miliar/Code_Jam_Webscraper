#include<cstdio>
#include<cstring>
#include<string>
#include<iostream>
#include<cmath>
#include<bitset>
using namespace std;
typedef long long int ll;
ll factor[11];
ll power(int a, int b)
{
	ll ans=1;
	for(int i=0;i<b;i++)
		ans*=a;
	return ans;
}
ll convert(int n, int base)
{
	ll ans=0;
	int count=0;
	while(n>0)
	{
		ans+=(n&1)*power(base,count);
		count++;
		n=n>>1;
	}
	return ans;
}
bool is_prime(ll num, int base)
{
	for(int i=2;i<=sqrt(num);i++)
	{
		if(num%i==0)
		{
			factor[base]=i;
			return false;
		}
	}
	return true;
}
int main()
{
	bool do_not_print;
	int count=0;
	printf("Case #1:\n");
	for(int i=32769;i<65537;i+=2)
	{
		if(count==50)
			return 0;
		do_not_print=false;
		for(int j=2;j<11;j++)
		{
			if(is_prime(convert(i,j),j))
			{
				do_not_print=true;
				break;
			}
		}
		if(!do_not_print)
		{
			// find the factors once for each base and print.
			cout<<bitset<16>(i).to_string()<<" ";
			for(int j=2;j<11;j++)
			{
				if(j!=10)
					cout<<factor[j]<<" ";
				else
					cout<<factor[j]<<endl;
			}
			count++;
		}
	}
}