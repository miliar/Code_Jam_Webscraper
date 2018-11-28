#include<bits/stdc++.h>
using namespace std;
int main()
{
	string s;
	long int j, k, i, h, t, c=0, cc=0, count;
	cin>>t;
	while(t>0)
	{
		cin>>s;
		for(i=0; i<s.length(); i++)
		{
			if(s[i]=='+')
			++c;
		}
		if(c==s.length())
		{
			cout<<cc<<"\n";
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
				//cout<<c<<"\n";
				
		}
		
		for(j=0; j<s.length(); j++)
		{
			if(s[j]=='+')
			{
				++count;
			}
		}
		if(count==s.length())
		{cout<<cc<<"\n";
			cc=0;
			count = 0;
			break;
		}
		}}
		
		t = t-1;
		s="";
		
		}
		return 0;
	}
	
