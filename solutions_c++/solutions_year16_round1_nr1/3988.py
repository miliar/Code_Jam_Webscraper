#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("A-large (1).in","r",stdin);
	freopen("1123.out","w",stdout);
	int t;
	cin>>t;
	int m=t;
	while(t--)
	{	
		string s;
		cin>>s;
		string a="";
		a+=s[0];
		for(int i=1;i<s.length();i++)
		{
			if(int(s[i])>=a[0])
			a.insert(0,1,s[i]);
			else
			a+=s[i];
		}
		cout<<"Case #"<<m-t<<": "<<a<<"\n";
		
	}
}
