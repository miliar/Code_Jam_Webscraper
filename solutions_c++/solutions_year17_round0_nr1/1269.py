//https://code.google.com/codejam/contest/3264486/dashboard
#include<bits/stdc++.h>
using namespace std;


int main()
{
	freopen("A-large (1).in","r",stdin);
	freopen("ggl.txt","w",stdout);
	int t;
	cin>>t;
	for(int tc=1;tc<=t;tc++)
	{
		string s;
		int n;
		cin>>s>>n;
		//string happy;
		//for(int i=0;i<n;i++)
		//happy[i]='+';
		int count=0;
		//cout<<"\ns.size()-n+1="<<s.size()-n+1<<"\n";
		for(int i=0;i<s.size()-n+1;i++)
		{
			if(s[i]=='-')
			{
				count++;
				for(int j=i;j<i+n;j++)
				{
					if(s[j]=='-')
					s[j]='+';
					else 
					s[j]='-';
				}
			}
		}
	//	cout<<"S="<<s<<"\n";
		//cout<<"\nhappy="<<happy<<"\ns.substr(s.size()-n-1,n))="<<s.substr(s.size()-n-1,n)<<"\n";
		//if(happy==(s.substr(s.size()-n-1,n)))
		int p=1;
		for(int i=0;i<s.size();i++)
		{
			if(s[i]=='-')
			{
				cout<<"Case #"<<tc<<": IMPOSSIBLE\n";
				p=0;
				break;
			}
		}
		if(p)
		cout<<"Case #"<<tc<<": "<<count<<"\n";
		//else
		//cout<<"Case #"<<tc<<": IMPOSSIBLE\n";
	}
}
