#include<stdio.h>
#include<iostream>
#include<map>

using namespace std;

string s, s1;

int main()
{
	int t, i, rt = 0;
	
	cin>>t;
	
	while(t--)
	{
		cin>>s;
	
		rt++;		
		s1.clear();
		
		s1.push_back(s[0]);
		
		for(i = 1; i < s.size(); i++)
		{
			if(s[i] != s[i-1])
			{
				s1.push_back(s[i]);
			}
		}
		
		if(s1[s1.size() - 1] == '+')
		{
			s1.pop_back();
		}
		
		cout<<"Case #"<<rt<<": "<<s1.size()<<"\n";		
	}
	
	return 0;
}
