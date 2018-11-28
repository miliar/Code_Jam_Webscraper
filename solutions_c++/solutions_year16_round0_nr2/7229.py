#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int main()
{
	long long t,i,l,ans,c;
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	char s[1001];
	cin>>t;
	for(c=1;c<=t;c++)
	{
		cin>>s;
		l=strlen(s);
		ans=0;
		while(1)
		{
			if(s[0]=='+')
			{
				for(i=0;i<l;i++)
				{
				   if(s[i]=='-')
				   {
				   	ans++;
				    break;
				   }
				   if(s[i]=='+')
				   s[i]='-';
				}
				if(i==l)
				break;
			}
			else
			{
				for(i=0;i<l;i++)
				{
					if(s[i]=='+')
					{
						ans++;
						break;
					}
					if(s[i]='-')
					s[i]='+';
				}
				if(i==l)
				ans++;
			}
		}
		cout<<"Case #"<<c<<": "<<ans<<endl;
	}
}
