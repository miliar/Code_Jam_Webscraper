#include<bits/stdc++.h>
using namespace std;

int main()
{
	long long t,i,j,c;
	char ch;
	string str;
	
	cin>>t;
	
	for(j=1;j<=t;j++)
	{
	stack<char>s;
	c=0;
	cin>>str;
	
	s.push(str[0]);
	
	for(i=1;i<str.size();i++)
	{
		ch=s.top();
		
		if(ch==str[i])
		{
			s.push(str[i]);
		}
		
		else
		{
		 c=c+1;
		 s.push(str[i]);	
		}
	}
	
	ch=s.top();
	
	if(ch=='-')
	c++;
	
	printf("Case #%lld: %lld\n",j,c);
	}
}
