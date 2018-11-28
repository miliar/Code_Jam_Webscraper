#include<bits/stdc++.h>
using namespace std;
int main()
{
freopen("B-large.in","r",stdin);
freopen("outyes.out","w",stdout);
	int t,n,k;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		char a[100];
		cin>>a;
		int l=0;
		int x=0;
		while(a[x]!='\0')
		{
		   l++;
		   x++;
	    }

		int flag=0;
		int count=0;
			for(int p=0;p<l;p++)
			{
				flag=1;
				if(a[p]!='+')
				{
					flag=0;
					break;
				}
			}
		while(flag!=1)
		{
			for( k=0;k<l;k++)
		{
		
				if(a[k]!=a[k+1])
				break;
			}
			for(int p=0;p<=k;p++)
			{
				if(a[p]=='+')
				a[p]='-';
				else
				a[p]='+';
			}
			for(int p=0;p<l;p++)
			{
				flag=1;
				if(a[p]!='+')
				{
					flag=0;
					break;
				}
			}
			count++;
		}
		cout<<"Case #"<<i<<": "<<count<<endl;
	}
}
