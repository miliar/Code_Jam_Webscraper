#include<stdio.h>
#include<iostream>
#include<string>
using namespace std;
int main()
{
	int testcases,t;
	cin>>testcases;
	for(t=0;t<testcases;t++)
	{
		int j,i=0;
		string s1,s;
		cin>>s;
		printf("CASE #%d: ",t+1);
		while(i<s.length())
		{
			j=i;
			while(i<s.length() && s[i]==s[j])
			{
				i++;
			}
			s1 += s[j];
		}
		if(s1[s1.length()-1]=='+')
		{
			s1.erase(s1.length()-1,1);
		}
//		cout<<s1<<endl;
		int count=0;
		for(i=0;i<s1.length();i++)
		{
			if(s1[i]=='+')
			{
				count++;
			}
		}
		int ans= 2*count;
		if(s1[0]=='-')
		{
			ans++;
		}
		cout<<ans<<endl;
	}
}
