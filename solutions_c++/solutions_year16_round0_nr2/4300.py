#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
//#define int long long
main() {
	freopen("largeinp.txt","r",stdin);
	freopen("largeouts.txt","w",stdout);
	int q;
	cin>>q;
	for(int z=1;z<=q;z++)
	{
		string s;
		cin>>s;
		int cur=0;
		if(s[0]=='+')
			cur=1;
		int ans=0;
		for(int i=1;i<s.length();i++)
		{
			if(s[i]=='+' && cur==0)
			{ans++; cur=1;}
			else if(s[i]=='-' && cur==1)
			{ans++; cur=0;}
		}
		
		if(cur==0)
			ans++;
		cout<<"Case #"<<z<<": "<<ans<<endl;

	}
	return 0;
}
