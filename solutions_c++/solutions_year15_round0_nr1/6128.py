#include<iostream>
#include<string>
#include<cstdio>

using namespace std;

int main()
{
	int t;
	cin>>t;
	string s;
	int smax,j=1;
	long long int invited,sum;
	while(j<=t)
	{
		invited=0,sum=0;
		cin>>smax;
		cin>>s;
		for(int i=1;i<=smax;i++)
		{
			sum=sum+(s[i-1]-48);
			if(sum<i)
				{
					invited=invited+(i-sum);
					sum=sum+(i-sum);
				}
			if(sum>=smax)
				break;
		}
		printf("case #%d: %lld\n",j++,invited);
	}
	return 0;
}