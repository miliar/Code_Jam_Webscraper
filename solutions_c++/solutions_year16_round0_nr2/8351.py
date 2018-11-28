#include <bits/stdc++.h>
using namespace std;
int count(string s)
{
	int f=0;
	for(int i=0;i<s.length();i++)
	{
		if(s[i]!='+')
			f=1;
	}
	if(f==0)
		return 0;
	f=0;
	if(s[0]=='+')
		f=1;
	for(int i=0;i<s.length();i++)
	{
		if(f==0)
		{
			if(s[i]=='-')
				s[i]='+';
			else
				break;
		}
		else
		{
			if(s[i]=='+')
				s[i]='-';
			else
				break;
		}
	}
	return 1+count(s);
}
int main(int argc, char const *argv[])
{
	long long int t;
	cin>>t;
	long long int ii=1;
	while(t--)
	{
		string s;
		cin>>s;
		
		cout<<"Case #"<<ii++<<": "<<count(s)<<endl;
	}
	return 0;
}