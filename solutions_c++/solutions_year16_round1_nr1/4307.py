#include<iostream>
#include<conio.h>
#include<string.h>
using namespace std;
main()
{
	int t,i;
	cin>>t;
	while(t-->0)
	{
		string s,a,b;
		
		cin>>s;
		a=a+s[0];
		//cout<<"add"<<a;
		for(i=1;i<s.length();i++)
		{
		//	cout<<s[i]<<a[0]<<"\n";
			if(s[i]<=a[0] && s[i]<=a[a.length()-1])
			{
				a=a+s[i];
			}	
			else if(s[i]>=a[a.length()-1] && s[i]>=a[0])
			{
				a=s[i]+a;
			}
			else
			{
				if(s[i]>=a[a.length()-1] && s[i]>=a[0])
				{
				b=s[i];
				a=b+a;
				}
				
				if(s[i]<=a[0] && s[i]>=a[a.length()-1])
				{
				b=s[i];
				a=a+b;	
				}
			}
		}
		cout<<"Case #t:"<<a<<"\n";
	}
}