#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long t,ans=0,max,no_here,req;
	string s;
	cin>>t;
	for(int x=1;x<=t;x++)
	{
		ans=0;
		req=0;
		scanf("%lld ",&max);
		cin>>s;
		no_here = s[0]-'0';
		for(int i=1;i<s.length();i++)
		{
			if(i>no_here&&s[i]!='0')
			{
				ans+=(i-no_here);
				no_here=i+s[i]-'0';
			}
			else
			no_here+=s[i]-'0';
		}
		cout<<"Case #"<<x<<": "<<ans<<"\n";
	}
	return 0;
}
