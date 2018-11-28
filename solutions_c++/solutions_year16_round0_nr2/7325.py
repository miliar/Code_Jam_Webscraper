#include <bits/stdc++.h>

using namespace std;

int main()
{	std::ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	for(int ti=1;ti<=t;ti++)
	{	string s;
		cin>>s;
		int ans=0;
		char prev='+';
		for(int i=s.length()-1;i>=0;i--)
		{	if(s[i]!=prev)ans++;
			prev=s[i];
		}
		cout<<"Case #"<<ti<<": "<<ans<<endl;
	}
}
