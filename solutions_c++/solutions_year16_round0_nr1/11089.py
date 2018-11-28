#include <iostream>
#include <stdlib.h>
#include <stdio.h>
using namespace std;
int present[10];
void update(long long n)
{
	while((n/10)!=0)
	{
		present[n%10]=1;
		n/=10;
	}
	present[n]=1;
}
int main(int argc, char const *argv[])
{
	int t,flag=0;
	long long n,temp;
	cin >> t;
	for(int i=1;i<=t;i++)
	{
		flag=0;
		for(int j=0;j<10;j++)
			present[j]=0;
		cin >> n;
		temp=n;
		if(n==0)
			cout << "Case #"<<i<<": "<<"INSOMNIA"<<endl;
		else if(n%2==1 && n%10!=5)
		{
			for(int j=1;j<=10;j++)
			{
				flag=0;
				n=temp*j;
				update(n);
				for(int k=0;k<10;k++)
				{
					if(present[k]!=1)
					{
						flag=1;
						break;
					}
				}
				if(flag==0)
				{
					cout << "Case #"<<i<<": "<<n<<endl;
					break;
				}
			}
		}
		else
		{
			for(int j=1;j<=1000;j++)
			{
				flag=0;
				n=temp*j;
				update(n);
				for(int k=0;k<10;k++)
				{
					if(present[k]!=1)
					{
						flag=1;
						break;
					}
				}
				if(flag==0)
				{
					cout << "Case #"<<i<<": "<<n<<endl;
					break;
				}
			}
		}
	}
	return 0;
}