#include <bits/stdc++.h>
using namespace std;
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);

	int T,no=0;
	cin>>T;
	while(T--)
	{
		string s;
		cin>>s;
		s+='+';
		int ans=0;
		for(int i=0;i<(int)s.size()-1;i++)
			if(s[i]!=s[i+1])
				ans++;
		cout<<"Case #"<<++no<<": "<<ans<<'\n';
	}
}