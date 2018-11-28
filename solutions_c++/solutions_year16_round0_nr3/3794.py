#include <iostream>
#include <math.h>
using namespace std;

long long int factor[11];

long long int isprime(long long int n,long long int j)
{
	for(long long int i=2;i*i<=n;i++)
	{
		if(n%i==0)
		{
			factor[j]=i;
			return 0;
		}
	}
	return 1;
}	

int main()
{
	long long int t,n,k,x,z,flag;
	cin>>t>>n>>k;
	z=0;
	long long int s[11];
	s[0]=0;s[1]=0;
	cout<<"Case #1:\n";
	for(long long int i=0;(i<((long long int)pow(2,n-2)))&&(z<k);i++)
	{
		flag=1;
		for(long long int j=2;(j<=10)&&(flag==1);j++)
		{
			long long int x=i,count=1;
			s[j]=0;
			while(count<=n-2)
			{
				if(x&1)
					s[j]+=(((long long int)pow(j,count)));
				x=x>>1;
				count++;
			}
			s[j]+=(((long long int)pow(j,n-1))+1);
			if(isprime(s[j],j)==1)
			{
				flag=0;
				break;
			}		
		}
		if(flag==1)
		{
			z++;
			cout<<s[10]<<" ";
			for(int j=2;j<=10;j++)
			{
				cout<<factor[j]<<" ";
			}
			cout<<endl;
		}
	}	
	return 0;
}		
