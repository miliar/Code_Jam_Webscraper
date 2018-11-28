#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	long long t,n,a,r,k;
	long long i,j,s=0;
	
	cin>>t;

	k=t;
	while(t--)
	{
	int *p=new int[20];
	p[0]={0};	
		cin>>n;
		if(n==0)
		{
			cout<<"Case #"<<k-t<<": "<<"INSOMNIA"<<endl;
			continue;
		}
		else
		{
			
			a=n;
			for(i=1;;i++)
			{
				a=n*i;
				while(a!=0)
				{
					r=a%10;
					p[r]=1;
					a=a/10;
				}
				s=0;
				for(j=0;j<10;j++)
				{
				 s=s+p[j];
				}
				if(s==10)
				{
					cout<<"Case #"<<k-t<<": "<<n*i<<endl;
					break;
				}
			}
		}
	}
}
