#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

int main()
{
	int i,t,n,ans,l,sum,j;
	string a;
	cin>>t;
	for(j=1;j<=t;j++)
	{
		ans=0;
		sum=0;
		cin>>n>>a;
		for(i=0;i<a.length();i++)
		{
			if(sum<(i))
			{
				ans++;
				sum++;
			}
			sum+=a[i]-'0';
		}
		cout<<"Case #"<<j<<": "<<ans<<endl;
	}
	return 0;
}