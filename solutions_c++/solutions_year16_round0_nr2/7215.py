#include<bits/stdc++.h>
using namespace std;
int main()
{	
	ifstream pe("B-large.in");
	ofstream out("qwe.out");
	
	int t;
	pe>>t;
	for(int q=0;q<t;q++)
	{
	string s,s1="";
	pe>>s;
	int l=s.size(),count=0,flag=0;char c='1';
	for(int i=l-1;i>=0;i--)
	{
		if(s[i]=='-'&&c!=s[i])
		{	c=s[i];
			++count;flag=1;
		}
		else if(s[i]=='+'&&flag==1&&c!=s[i])
		{	c=s[i];
			++count;
		}
	
	}
	out<<"Case #"<<q+1<<": "<<count<<"\n";
	
	}	
	
}
