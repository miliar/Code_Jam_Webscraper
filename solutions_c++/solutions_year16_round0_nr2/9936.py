#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long int t,l,d,b,c,n,i,j,k;
	cin>>t;
	string s;
	for(i=1;i<=t;i++)
	{
		cin>>s;
		c=0;b=0;
		n=s.length();
		for(d=0;;d++)
		{
			b=0;
			c=0;
			for(l=0;l<n;l++)
			{
				if(s[l]=='+')
				{
					b++;
				}
			}
			if(b==n)
			{
				cout<<"Case #"<<i<<": "<<d<<endl;
				break;
			}
			else
			{
				for(j=n-1;j>=0;j--)
				{
					if(s[j]=='-')
					{
						c=1;
						break;
					}
				}
				if(c==1)
				{	
					for(k=0;k<=j;k++)
					{
						if(s[k]=='+')
							s[k]='-';
						else
							s[k]='+';
					}
				}
			}	
		}
	}
}
