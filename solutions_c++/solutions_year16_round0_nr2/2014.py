#include <bits/stdc++.h>
using namespace std;

string shorten(string s)
{
	for(int i=1;i<s.length();i++)
	{
		if(s[i]==s[i-1])
		{
			s=s.substr(0,i)+s.substr(i+1);
			i--;
			//cout<<s<<" ";
		}
	}
	return s;
}

int answer(string s, int l)
{
	int ctr=l;
	if(s[l-1]=='+') ctr--;	
	return ctr;	
}

int main()
{
	int t;
	cin>>t;
	string s;
	
	for(int tt=1;tt<=t;tt++)
	{
		cin>>s; s=shorten(s); int l=s.length();
		int ctr=answer(s,l);
		cout<<"Case #"<<tt<<": "<<ctr<<endl;				
	}
}
