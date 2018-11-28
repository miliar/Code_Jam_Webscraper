#include<iostream>
#include<cstring>
#include<fstream>
#include<cstdio>
using namespace std;
string s;

int func(string s,int n)
{
	int ans=0,j=0,end=s.length();
	
	for(int i=0;i<s.length();i++)
	{
		if(j==end-1)
		{
			if(s[i]=='-')
			{
				ans++;
			}
		}
		else
		{
			if(s[i]!=s[i+1])
			{
				ans++;
			}
		}
		j++;
	}
	return ans;
}

int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cin>>s;
		int ans=func(s,i);
		cout<<"Case #"<<i<<": "<<ans<<endl;	
	}
}
