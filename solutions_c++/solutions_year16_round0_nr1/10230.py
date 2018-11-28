#include<iostream>
#include<stdlib.h>
using namespace std;
int main()
{
	int cases;
	cin>>cases;
	for(int p=1;p<=cases;p++)
	{
		int A[10]={0},fl,n,i,k=1,n1,fl2=0,n2;
		cin>>n;
		n1=n;
		while(1)
		{
			char s[1000000];
			itoa(n1,s,10);
			for(i=0;s[i]!='\0';i++)
			{
				A[s[i]-'0']++;
			}
			fl=0;
			for(i=0;i<10;i++)
			{
				if(A[i]<1)
				{
					fl=1;
					break;
				}
			}
			if(fl==0)
			{
				break;
			}
			else
			{
				k++;
				n2=n1;
				n1=n*k;
			}
			//cout<<"*"<<n1<<"\n";
			if(n2==n1)
			{
				fl2=1;
				break;
			}
		}
		if(fl2==0)
		{
			cout<<"Case #"<<p<<": "<<n1<<"\n";
		}
		else
		{
			cout<<"Case #"<<p<<": "<<"INSOMNIA\n";
		}
	}
	return 0;
}