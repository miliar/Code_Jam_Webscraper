#include<iostream>
#include<string.h>
using namespace std;
int main()
{
	int t,x;
	cin>>t;
	for(x=1; x<=t; x++)
	{
		char s[101],temp;
		cin>>s;
		long int l=strlen(s),ans=0,i;
		if(s[l-1]=='-')
		  ans++;
		for(i=l-1,temp=s[l-1]; i>=0; i--)
		{
			if(s[i]!=temp)
			{
				temp=s[i];
				ans++;
			}
		}
		cout<<"Case #"<<x<<": "<<ans<<"\n";
	}
}
