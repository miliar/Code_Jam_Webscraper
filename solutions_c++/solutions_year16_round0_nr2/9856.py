#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out500.out","w",stdout);
	int t;
	cin>>t;
	for(int i=1;i<=t;++i)
	{
		string s;
		cin>>s;
		int len=s.length();
		int cou=0;
		int where=1;
		char ch=s[0];
		for(int where=1;where<=len-1;where++)
		{
			if(s[where]!=ch)
			{
				for(int i=0;i<where;++i)
					s[i]=s[where];
				ch=s[where];
				cou++;
			}
		}
		if(s[len-1]=='-')
			cou++;
		cout<<"Case #"<<i<<": "<<cou<<endl;
	}
	return 0;
}


