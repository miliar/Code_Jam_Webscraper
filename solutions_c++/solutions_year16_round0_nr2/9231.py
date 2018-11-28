#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out10.out","w",stdout);
	int t;
	cin>>t;
	for(int i=1;i<=t;++i)
	{
		string s;
		cin>>s;
		int k=s.length();
		int count=0;
		int where=1;
		char c=s[0];
		while(where<=k-1)
		{
			if(s[where]!=c)
			{
				for(int i=0;i<where;++i)
					s[i]=s[where];
				c=s[where];
				count++;
			}
			where++;
		}
		if(s[k-1]=='-')
			count++;
		cout<<"Case #"<<i<<": "<<count<<endl;
	}
	return 0;
}


