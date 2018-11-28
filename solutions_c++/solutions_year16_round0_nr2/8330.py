#include<bits/stdc++.h>
using namespace std;
int main()
{
	string s;
	long long int j, k, i, h=1, t, c=0, cc=0, co=0,d;
	cin>>t;
	while(t>0)
	{	c=0;
		cin>>s;
		for(i=0; i<s.length(); i++)
		{
			if(s[i]=='+')
			++c;
		}
		if(c==s.length())
		{
			cout<<"Case #"<<h<<": "<<cc<<"\n";
			co=0;
		}
		else
		{
		while(true)
		{
			if(s[0]=='+')
			{for(i=0; i<s.length();i++)
			{	
			
				if(s[i]=='+')
				{
					s[i]='-';
					//++cc;
				}
				else
				{i=0;
				
					break;
				}
			}
			++cc;
			
		//	cout<<cc<<"\n";
			//break;
			}
			else
			{
		for(i=0; i<s.length();i++)
		{

				
				if(s[i]=='-')
				{
					s[i]='+';
					
				}
				else
				{i=0;
				//++cc;
				//cout<<cc<<"\n";
					break;
				}
				
				}
				++cc;
			//	cout<<cc<<"\n";
				//break;
				
				
		}
		
		for(j=0; j<s.length(); j++)
		{
			if(s[j]=='+')
			{
				++co;
			}
		}
		if(co==s.length())
		{cout<<"Case #"<<h<<": "<<cc<<"\n";;
			cc=0;
			co = 0;
			break;
		}
		co=0;
		}}
		
		t = t-1;
		s="";
		++h;
		cc=0;
		co=0;
		}
		//return 0;
	}
	
