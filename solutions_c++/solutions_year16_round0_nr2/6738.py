#include<iostream>
#include<cstring>
using namespace std;
int main()
{	freopen("B-large.in","r",stdin);
	freopen("Blarge.txt","w",stdout);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		string a;
		cin>>a;
		int l=a.size(),c,f;
		if(a[l-1]=='-')
		{
			c=1;f=1;
		}
		else {c=0;f=0;}
		
		for(int j=l-2;j>=0;j--)
		{
			if(a[j]=='+')
			{
				if(f==1)
				{
					c++;
					f=0;
				}
			}
			else
			{
				if(f==0)
				{
					c++;
					f=1;
				}
			}
		}
		cout<<"Case #"<<i<<": "<<c<<"\n";
	}
}
