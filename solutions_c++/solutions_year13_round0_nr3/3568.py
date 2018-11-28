#include<iostream>
#include<cstring>
#include<fstream>
#include <sstream>
#include<stdlib.h>
#include<cmath>
#define MAX 1000
using namespace std;

bool ispalindrome( string s)
{
	 long len=s.length();
	
	for(int i=0;i<len/2;i++)
		if(s[i]!=s[len-i-1])
			return false;
	return true;
}


long long convert(char s[])
{
	return atol(s);
}


int main()
{
	
	
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int t;int p=0;
	cin>>t;
	
	
	
	while(t--)
	{
		char s[MAX],q[MAX]; int count=0;
		cin>>s;		//range
		cin>>q;		//range
		
	
		
		long long a,b;
		double qt;
		
		qt=sqrt(convert(s));
	
		a=qt;
		
		if(qt>a)
		a=a+1;
		
		
		
		b=convert(q);
		
		for(int i=a;i*i<=b;i++)
		{
			ostringstream ss,sp;
			 ss<<i;
			 sp<<i*i;
			 
		
			if(ispalindrome(ss.str()) && ispalindrome(sp.str()))
				{
					count++;
					//cout<<ss.str()<<"\n";
				}
			
		}
				 
		cout<<"Case #"<<p+1<<": "<<count<<endl;
		p++;
			
	}
	
}
