#include<iostream>
#include<string.h>
#include<bits/stdc++.h>
using namespace std;
int calculate(string s)
{
	int p[s.length()];
	int m[s.length()];
	if(s[0] == '+')
	{
		p[0] = 0;
		m[0] = 1;
	}
	if(s[0] == '-')
	{
		p[0] = 1;
		m[0] = 0;
	}
	
	for(int i=1;i<s.length();i++)
	{
		if(s[i] == '+')
		{
			p[i] = p[i-1];
			m[i] = min(p[i-1]+1,m[i-1]+2);
		}
		else if(s[i] == '-')
		{
			m[i] = m[i-1];
			p[i] = min(m[i-1]+1,p[i-1]+2);
		}
	}
	return p[s.length()-1];
}

int main()
{
	int t;
	string s;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cin>>s;
		cout<<"Case #"<<i<<": "<<calculate(s)<<endl;
	}
	return 0;
}	
