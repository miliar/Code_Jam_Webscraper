#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out7.out","w",stdout);
	int t,n,k;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		char s[100];
		cin>>s;
		int length=0;
		int x=0;
		while(s[x]!='\0')
		{
		   length++;
		   x++;
	    }
//	    cout<<s<<endl;
		int done=0;
		int count=0;
			for(int p=0;p<length;p++)
			{
				done=1;
				if(s[p]!='+')
				{
					done=0;
					break;
				}
			}
		while(done!=1)
		{
			for( k=0;k<length;k++)
			{
//				cout<<"Hello"<<endl;
				if(s[k]!=s[k+1])
				break;
			}
			for(int p=0;p<=k;p++)
			{
				if(s[p]=='+')
				s[p]='-';
				else
				s[p]='+';
			}
			for(int p=0;p<length;p++)
			{
				done=1;
				if(s[p]!='+')
				{
					done=0;
					break;
				}
			}
			count++;
		}
		cout<<"Case #"<<i<<": "<<count<<endl;
	}
}
