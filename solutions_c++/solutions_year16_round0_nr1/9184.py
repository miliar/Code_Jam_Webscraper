#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output","w",stdout);
	long long int n,t,k=1;
	cin>>t;
	for(k=1;k<=t;k++)
	{
		long long int a[10]={0},i=1,x,p,count=0;
		cin>>n;
		if(n==0)
		cout<<"Case #"<<k<<": INSOMNIA\n";
		else
		{
			x=n;
			while(count<10)
			{
				x=n*i;
				while(x>0)
				{
					p=x%10;
					x=x/10;
					if(a[p]==0)
					{
						count++;
						a[p]=1;	
					}	
				}
				i++;
			}	
			cout<<"Case #"<<k<<": "<<(i-1)*n<<"\n";
		}
	}
	return 0;
}
