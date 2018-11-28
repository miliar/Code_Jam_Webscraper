#include<iostream>
#include<conio.h>

using namespace std;

int main()
{
	int a[1001],b,c,t,x;
	char z[1001];
	cin>>t;
	for(int j=0;j<t;j++)
	{
		b=0;
		c=0;
		cin>>x;
		cin>>z;
		for(int i=0;i<=x;i++)
			a[i]=z[i]-48;
		for(int i=0;i<=x;i++)
		{
			if(b>=i && a[i]>0)
			{
				//cout<<"yes"<<b<<i<<a[i];
				b+=a[i];
				
			}
			else if(a[i]>0)
			{
				//cout<<"no"<<b<<i<<a[i];
				c+=i-b;
				b+=a[i]+i-b;
				
			}
		}
		cout<<"Case #"<<j+1<<": "<<c<<endl;
	}
	return 0;
}
