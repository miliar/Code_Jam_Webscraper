#include <bits/stdc++.h>

using namespace std;


int main()
{
	int T;
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>T;
	
	
	for(int ii=1;ii<=T;ii++)
	{
		string s;
		int ans=0;
		int prev = -1;
		cin>>s;
		int sz = s.size();
		if(s[0]=='-')
		{
			prev = 0;
		}
		else
		{
			prev = 1;
		}
		for(int i=1;i<sz;i++)
		{
			if(s[i]=='-')
			{
				if(prev==1)
				{
					ans++;
					prev=0;
				}
			}
			else
			{
				if(prev==0)
				{
					ans++;
					prev=1;
				}
			}
		}
		if(prev==0)
		{
			ans++;
		}
		cout<<"Case #"<<ii<<": "<<ans<<"\n";
	}

	return 0;
}