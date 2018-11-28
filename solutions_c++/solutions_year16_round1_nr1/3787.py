#include <bits/stdc++.h>
using namespace std;
int main()
{
	string ans,s;
	long int x,y,t;
	cin>>t;
	
	for(x=1;x<=t;x++)
	{
		cin>>s;
		ans="";
		ans=s[0];
		for(y=1;y<s.size();y++)
		{
			if(s[y]>=ans[0])
			ans=s[y]+ans;
			else
			ans=ans+s[y];
		}
		cout<<"Case #"<<x<<": "<<ans<<endl;
	}
	return 0;
}