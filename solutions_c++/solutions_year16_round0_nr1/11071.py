#include<iostream>
#include<vector>
using namespace std;
long t,n,i,c,left,j,dig,f;
	long a[10];
int main()
{
	
	cin>>t;
	for(i=0;i<t;i++)
	{
		cin>>n;
		for(j=0;j<10;j++)
		{
			a[j]=0;
		}
		left=10;
		if(n==0)
		{
			cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
			continue;
		}
		for(j=1;left>0;j++)
		{
			c=n*j;
			f=c;
			while(c)
			{
				dig=c%10;
				c=c/10;
				if(a[dig]==0)
				{
					a[dig]=1;
					left--;
					if(left==0)
					{	cout<<"Case #"<<i+1<<": "<<f<<endl;
						break;
					}
				}
				
			}
		}
	}
	return 0;
}
