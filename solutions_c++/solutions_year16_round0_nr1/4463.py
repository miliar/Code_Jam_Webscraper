#include <iostream>
using namespace std;

int main()
{
	long long int t,n;
	cin>>t;
	for(int z=1;z<=t;z++)
	{
		cin>>n;
		if(n==0)
		{
			cout<<"Case #"<<z<<": INSOMNIA"<<endl;
			continue;
		}
		long long int a[10],flag=0,x,i;
		for(i=0;i<10;i++)
			a[i]=0;
		for(i=1;flag!=1;i++)
		{
			x=i*n;
			while(x!=0)
			{
				a[x%10]=1;
				x/=10;
			}
			flag=1;
			for(int j=0;j<10;j++)
			{
				if(a[j]==0)
				{
					flag=0;
					break;
				}
			}
		}
		x=(i-1)*n;
		cout<<"Case #"<<z<<": "<<x<<endl;
	}
	return 0;
}
