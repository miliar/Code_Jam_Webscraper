#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;
int main()
{
	int tc;
	cin>>tc;
	for(int t=1;t<=tc;t++)
	{
		int n;
		cin>>n;
		string s;
		cin>>s;
		int sum=0;
		int ans=0;
		for(int i=0;i<n+1;i++)
		{
			if(sum<i)
			{
				ans=ans+i-sum;
				sum=i;
			}
			sum=sum+(s[i]-'0');
		}
		cout<<"Case #"<<t<<": "<<ans<<"\n";
	}
	return 0;
}
