#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
	int t=0,testcases;
	cin>>testcases;
	while(testcases--)
	{
		t++;
		int digit[10]={0}, n,count=0;
		cin>>n;
		cout<<"CASE #"<<t<<": ";
		if(n==0)
		{
			cout<<"INSOMNIA\n";
		}
		else
		{
			int temp2=n;
			while(count<10)
			{
				int temp= n;
				while(temp>0)
				{
					int op = temp%10;
					if(digit[op]==0)
					{
						digit[op]=1;
						count++;
					}
					temp= temp/10;
				}
				n= n+ temp2;
			}
			cout<<n-temp2<<endl;
		}
	}
	return 0;
}
