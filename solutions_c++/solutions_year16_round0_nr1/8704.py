#include<iostream>
using namespace std;
int main()
{
	int t;
	int b=1;
	cin>>t;
	while(t--)
	{
		long long n;
	cin>>n;
	if(n==0)
	{
		cout<<"Case #"<<b<<": INSOMNIA"<<endl;
		b++;
	}
	else
	{
	bool check[10];
	for(int j=0;j<10;j++)
		check[j]=0;
	long long n1=0;
	int a=1;
	int k=1;
	while(a)
	{
		n1=n*k;
		int rem=0;
		do
		{
			rem=n1%10;
			n1=n1/10;
			if(check[rem]==0)
			{
				check[rem]=1;
			}	
		}while(n1>0);
		bool t1=0;
		for(int i=0;i<10;i++)
		{
			if(check[i]==0)
			{
				t1=1;
				break;
			}
			}	
			if(t1==0)
			{
				cout<<"Case #"<<b<<": "<<n*(k)<<endl;
				a=0;
			}
		k++;
	}
	b++;
}
		}	
	return 0;
}
