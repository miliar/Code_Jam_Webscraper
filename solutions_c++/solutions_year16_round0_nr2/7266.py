#include<stdio.h>
#include<queue>
#include<iostream>
using namespace std;
int steps;
string sub(string pattern)
{
	while(pattern[pattern.length()-1]=='+')
	pattern=pattern.substr(0,pattern.length()-1);
	return pattern;
}

string strrev(string pattern)
{
	char temp;
	for(int i=0;i<pattern.length()/2;i++)
	{
			temp=pattern[i];
			pattern[i]=pattern[pattern.length()-1-i];
			pattern[pattern.length()-1-i]=temp;
	}
	if(pattern[pattern.length()-1]=='+')
	{
			pattern=sub(pattern);
			steps++;
	}
	for(int i=0;i<pattern.length();i++)
	{

			if(pattern[i]=='+')
			pattern[i]='-';
			else
			pattern[i]='+';
	}
	return pattern;
}


int main()
{
	int test_case=0;
	cin>>test_case;

	for(int i=0;i<test_case;i++)
	{
		string pattern;
		steps=0;
		cin>>pattern;
		while(pattern.length()>0)
		{
				pattern=sub(pattern);
				pattern=strrev(pattern);
				steps++;
				//cout<<pattern<<endl;
		}

		//cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
		cout<<"Case #"<<i+1<<": "<<steps-1<<endl;
	}
	return 0;
}
