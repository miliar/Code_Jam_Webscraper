#include<iostream>
#include<string.h>
using namespace std;
int main()
{
	int t,x,l,i,p,q;
	char s[1001],s1[2002];
	cin>>t;
	for(x=1; x<=t; x++)
	{
		cin>>s;
		l=strlen(s);
		s1[1000]=s[0];
		for(i=1,p=1000,q=1000; i<l; i++)
		{
			if(s[i]>=s1[p])
			{
				s1[--p]=s[i];
			}
			else
			{
				s1[++q]=s[i];
			}
		}
		cout<<"Case #"<<x<<": ";
		for(; p<=q; p++)
		{
			cout<<s1[p];
		}
		cout<<"\n";
	}
}
