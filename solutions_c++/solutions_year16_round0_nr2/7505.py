#include<iostream>
using namespace std;

long int pancake(string s);

int t;
long int cnt=0;
string s[101];

inline bool check(string s)
{
	for(int i=0;s[i]!='\0';i++)
		if(s[i]!='+')
			return 0;
	return 1;
}

int main()
{
	cin>>t;
	for(int i=1;i<=t;i++)
		cin>>s[i];
	for(int i=1;i<=t;i++)
	{
		cnt=0;
		cout<<"Case #"<<i<<": "<<pancake(s[i])<<endl;
	}
	
	return 0;
}

long int pancake(string s)
{	
	int i;
	if(check(s))
		return cnt;
	
	char x=s[0];
	
	for(i=0;s[i]!='\0';i++)
	{
		if(s[i]!=x)
		{
			++cnt;
			x=s[i];
		}
			
	}
	
	if(s[i-1]=='+')
		return cnt;	
	
	return cnt+1;
}
