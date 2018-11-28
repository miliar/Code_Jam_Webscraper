#include <bits/stdc++.h>
using namespace std;
int T,l;
string s,ans;
int main()
{
	//ifstream cin("A-large.in");
	//ofstream cout("1.out");
	cin>>T;
	for(int cases=1; cases<=T; cases++)
	{
		cin>>s;
		l=s.size();
		ans="";
		ans=ans+s[0];
		for(int i=1; i<l; i++)
		{
			if(ans[0]>s[i])ans=ans+s[i];
			else ans=s[i]+ans;
		}
		cout<<"Case #"<<cases<<": "<<ans<<endl;
	}
	return 0;
}
