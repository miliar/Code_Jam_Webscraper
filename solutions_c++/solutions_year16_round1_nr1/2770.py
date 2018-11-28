#include<bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		string s;
		cin>>s;
		string ans="";
		for(int j=0;j<s.length();j++)
		{
			if(ans=="")
				ans+=s[j];
			else if(ans[0]<=s[j])
				ans=s[j]+ans;
			else
				ans+=s[j];
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}
