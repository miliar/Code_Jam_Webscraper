#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	int T;
	cin>>T;
	for(int i=1;i<=T;++i)
	{
		int n;
		cin>>n;
		string a;
		cin>>a;
		int ans=0,beforepeople=a[0]-'0';
		for(int k=1;k<=n;++k)
		{
			if(beforepeople>=n)	break;
			if(a[k]=='0')	continue;
			if(beforepeople>=k)
			{
				beforepeople+=a[k]-'0';
			}
			else
			{
				ans=ans+k-beforepeople;
				beforepeople=k+a[k]-'0';
			}
		}
		printf("Case #%d: %d\n",i,ans);
	}
}
