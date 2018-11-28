#include <iostream>
#include<stdio.h>
using namespace std;

int main() {
    freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	int digits[10];

	for(int i=1;i<=t;i++)
	{
		int n;
		scanf("%d",&n);
		if(n==0)
		{
			cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
			continue;
		}
		int temp=n;
		for(int j=0;j<10;j++)
		digits[j]=0;
		int j;
		while(n>0)
		{
			digits[n%10]++;
			n=n/10;
		}
		int rem=0,carry=0,k=2;
		while(true)
		{
			n=k*temp;
			while(n>0)
			{
				digits[n%10]++;
				n=n/10;
			}
				for(j=0;j<10;j++)
			{
				if(digits[j]==0)
				break;
			}
			if(j==10)
			break;
			k++;
		}
		cout<<"Case #"<<i<<": "<<k*temp<<endl;

	}
	return 0;
}
