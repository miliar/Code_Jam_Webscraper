#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,T;
	string s;
	cin>>t;
	T=t;
	while(t--)
	{
		int ans=0;
		cin>>s;
		if(s[0]=='-')
		{
			ans=1;
		}
		for(int i=0;i<s.length();i++)
		{
			if((s[i]=='+')&&(i<(s.length()-1))&&(s[i+1]=='-'))
			{
				ans=ans+2;
			}
		}
		cout<<"Case #"<<T-t<<": "<<ans<<endl;	
	}
	return 0;
}
