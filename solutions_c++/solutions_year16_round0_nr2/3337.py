#include <iostream>
#include<cstring>
//#include<stdlib>
using namespace std;

int main() {
	// your code goes here
	int t,i,j,l,m,p,z;
	cin>>t;
	for(z=1;z<=t;z++)
	{
		string s;
		cin>>s;
		l=s.length();
		j=l-1;
		for(j=l-1;j>=0;j--)
		{
			if(s[j]=='-')
			break;
		}
		m=0;p=0;
		if(s[j]=='-')
		{
		m=0;
		p=1;
		}
		else if(s[j]=='+')
		m=1;
		for(i=j;i>=0;i--)
		{
			if(s[i]=='-')
			{
				if(m==1)
				{p++;
				m=0;
				}
				
			}
			if(s[i]=='+')
			{
				if(m==0)
				{
					p++;
					m=1;
				}
			}
		    
		}
		cout<<"Case #"<<z<<": "<<p<<"\n";
		
	}
	return 0;
} 