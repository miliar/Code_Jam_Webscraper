#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out20.out","w",stdout);
	int t,x;
	cin>>t;
	for(x=1;x<=t;x++)
	{
		string s;
		cin>>s;
		int len=s.length();
		int c=0;
		int where=1;
		char ch=s[0];
		for(int where=1;where<=len-1;where++)
		{
			if(s[where]!=ch)
			{
				for(int i=0;i<where;++i)
					s[i]=s[where];
				ch=s[where];
				c++;
			}
		}
		if(s[len-1]=='-')
			c++;
		cout<<"Case #"<<x<<": "<<c<<endl;
	}
	return 0;
}
