#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<iostream>
using namespace std;
int T;
string s;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	cin>>T;
	for(int I=1;I<=T;I++)
	{
		cout<<"Case #"<<I<<": ";
		cin>>s;
		s+='+';
		int ans=0;
		for(int i=1;i<s.size();i++)
			ans+=s[i]!=s[i-1];
		cout<<ans<<endl;
	}
	return 0;
}

