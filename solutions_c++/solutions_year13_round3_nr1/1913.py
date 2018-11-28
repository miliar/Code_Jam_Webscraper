#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;
bool isVowel(char ch)
{
	return ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u';
}
bool correct(string s,int n)
{
	int l=s.length();
	bool present;
	for(int i=0;i<=l-n;i++)
	{
		string ss=s.substr(i,n);
		bool c=true;
		for(int j=0;j<n;j++)
		{
			if(isVowel(ss[j]))
			{
				c=false;
				break;
			}
		}
		if(c)
		return true;
	}
	return false;
}
int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int n;
		string name;
		cin>>name;
		cin>>n;
		int l=name.length(),count=0;
		for(int j=0;j<=l-n;j++)
		{
			for(int k=n;k<=l-j;k++)
			{
				string s=name.substr(j,k);
				if(correct(s,n))
					count++;
			}
		}
		cout<<"Case #"<<i<<": "<<count<<"\n";
	}
}
