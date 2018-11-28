#include<bits/stdc++.h>
using namespace std;
int main()
{
  freopen("B-large.in","r",stdin);
  freopen("out2.out","w",stdout);	
int t,n,k;
	cin>>t;
	for(int i=1;i<=t;i++)
	{	char s[101];
		int flag=0;
		cin>>s;
		int len=0;
		int x=0;
		while(s[x]!='\0')
		{   len++;
		   x++;
	    }
		int flips=0;
		for(int p=0;p<len;p++)
		{	flag=1;
			if(s[p]!='+')
			{	flag=0;
				break;
			}
		}
		while(flag!=1)
		{	for( k=0;k<len;k++)
			{	if(s[k]!=s[k+1])
				break;
			}
			for(int p=0;p<=k;p++)
			{	if(s[p]=='+')
				s[p]='-';
				else
				s[p]='+';
			}
			for(int p=0;p<len;p++)
			{	flag=1;
				if(s[p]!='+')
				{	flag=0;
					break;
				}
			}
			flips++;
		}
		cout<<"Case #"<<i<<": "<<flips<<endl;
	}
}
