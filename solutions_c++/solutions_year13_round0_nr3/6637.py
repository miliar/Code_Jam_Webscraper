#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
using namespace std;
vector<long long int> v;
vector<int> d;

int pal(long long int x)
{
	int n,i,j,flag;
	d.clear();
	while(x)
	{
		d.push_back(x%10);
		x=x/10;
	}	
	n=d.size();
	flag=1;
	if(n %2)
	{
		for(i=0;i<(n-1)/2;i++)
		{
			if(d[i]!=d[n-i-1])
			{
				flag=0; 
				break;
			}
		}
	}
	
	else
	{
		for(i=0;i<n/2;i++)
		{
			if(d[i]!=d[n-i-1])
			{
				flag=0; 
				break;
			}
		}
	}
	if(flag)
		return 1;
	else
		return 0;
}
int main()
{
	long long int n,i,j,k,t,a,b,count;
	for(i=1;i<=10000000;i++)
	{
		if(pal(i))
		{
			if(pal(i*i))
				v.push_back(i);
		}
	}
	/*for(i=0;i<v.size();i++)
	{
		cout<<v[i]<<" ";
	}*/
	scanf("%lld\n",&t);
	for(k=1;k<=t;k++)
	{
		scanf("%lld%lld",&a,&b);
		for(i=0;i<v.size();i++)
		{
			if(v[i]>=sqrt(a))
				break;
		}
		count=0;
		while(v[i]<=sqrt(b))
		{
			i++;
			count++;
		}
		printf("Case #%lld: %lld\n",k,count);
	}
	return 0;
}
