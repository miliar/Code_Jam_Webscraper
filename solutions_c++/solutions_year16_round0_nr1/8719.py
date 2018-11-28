#include<iostream>
using namespace std;
//int a[10];
int main()
{
	int t,p=1;
	cin>>t;
	while(p<=t)
	{
		unsigned long long n;
		cin>>n;
		if(n==0)
			cout<<"Case #"<<p<<": "<<"INSOMNIA"<<"\n";
	else{
		int i=1,a[10]={0};
		while(1)
		{	int check=0;	
			 unsigned long long temp=n*i;
			while(temp)
			{
				a[temp%10]=1;
				temp=temp/10;
			}									
			for(int k=0;k<10;k++)
				if(a[k]==1)
					check++;
			if(check==10)
			 {
				cout<<"Case #"<<p<<": "<<n*i<<"\n";
				break;
			}
			i++;			
		}}
		p++;
	}
	return 0;
}