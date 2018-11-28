#include<iostream>
#include<fstream>
#include<cstdio>
using namespace std;
int main ()
{
	int t,s,count=0,sum=0;
	string g;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("a-small.out","w",stdout);
	cin>>t;
	for(int z=1;z<=t;z++)
	{
		cin>>s;
		cin>>g;
		count=sum=0;
		sum=g[0]-48;
		for(int i=1;i<=s;i++)
		{
			if(i>sum)
			{
				count+=i-sum;
				sum=i;
				//sum=g[i]-48;
			}
			sum+=g[i]-48;
		}
		printf("Case #%d: %d\n",z,count);
	}
	return 0;
}
