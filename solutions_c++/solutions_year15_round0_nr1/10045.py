#include <iostream>
#include <string>
using namespace std;

int main()
{
	int ans,i,n,final,t;
	string s;
	cin>>t;
	for(int j=1;j<=t;j++)
	{
		cin>>n;
		cin>>s;
		ans=0;
		final=0;
		for(i=0;i<=n;i++)
		{
			if(s[i]>'0')
			{
				if(i<=ans)
					ans+=(s[i]-'0');
				else
				{
					final+=(i-ans);
					ans+=(final+(s[i]-'0'));
				}
			}
		}
		cout<<"Case #"<<j<<": "<<final<<endl;
	}
	return 0;
}