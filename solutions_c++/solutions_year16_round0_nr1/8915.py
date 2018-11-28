#include<iostream>
using namespace std;
int check(long long int a,long long int mark[20])
{
	while(a!=0)
	{
		mark[a%10]|=1;
		a/=10;
	}
	for(int i=0;i<=9;i++)
		if(!mark[i])
			return 0;
		return 1;
}
int main()
{
	int t;
	cin>>t;
	for(int j=1;j<=t;j++)
	{

		long long int a,b,mark[20]={0};
		cin>>a;
		if(a==0)
		{
			cout<<"Case #"<<j<<": "<<"INSOMNIA\n";
		}
		else
		{
			b=a;
			while(!check(a,mark))
			{
				a+=b;
			}
			cout<<"Case #"<<j<<": "<<a<<endl;
		}
	}
}