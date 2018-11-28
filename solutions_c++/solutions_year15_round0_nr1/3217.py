#include<iostream>
#include<cstdio>
#include<string>
using namespace std;

int main()
{
	int t;
	cin>>t;
	int curr;
	for(curr=1;curr<=t;curr++)
	{
		int sum=0;
		int smax;
		int ans=0;
		string input;
		cin>>smax>>input;
		sum=input[0]-'0';
		int i;
		for(i=1;i<=smax;i++)
		{
			if(input[i]=='0') continue;
			if(sum>=i)
			{
				sum+=input[i]-'0';
				continue;
			}
			ans+=(i-sum);
			sum+=(i-sum);
			sum+=input[i]-'0';
		}
		printf("Case #%d: %d\n",curr,ans);
	}
	return 0;
}
