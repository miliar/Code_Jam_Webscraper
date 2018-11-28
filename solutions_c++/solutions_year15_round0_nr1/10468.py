#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int t,i,n,c=0,f=0,j;
	char a[10];
	cin>>t;
	for(i=0;i<t;++i)
	{
		cin>>n;
		scanf("%s",a);
		c+=a[0];
		c=c-48;
		for(j=1;j<=n;++j)
		{
			if(c<j)
			{
				
				f+=j-c;
				c+=j-c;
				c+=a[j];
				c=c-48;
				
			}
			else
			{
				c+=a[j];
				c=c-48;	
			}
		}
		cout<<"Case #"<<i+1<<": "<<f<<endl;
		f=0;
		c=0;
	}
	return 0;
}
