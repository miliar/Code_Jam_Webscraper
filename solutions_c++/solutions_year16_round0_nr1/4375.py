#include<iostream>
using namespace std;
int chk_arr(int a[])
{
	int i;
	for(i=0;i<10;i++)
	{
		if(a[i]!=i)
			return 0;	
	}
	return 1;
}
int main()
{
	int t;
	int c=1;
	cin>>t;
	while(t--)
	{
		int i,mul,flag;
		long long n,o,j;
		cin>>n;
		j=n;
		mul=2;
		flag=1;
		int a[10]={10};
		if(j==0)
			cout<<"Case #"<<c<<": INSOMNIA"<<endl;
		else
		{
			while(chk_arr(a)==0)
			{
				if(flag==1)
					o=n;
				flag=0;
				i=n%10;
				a[i]=i;
				n=n/10;
				if(n==0)
				{
					n=j*mul;
					mul++;
					flag=1;
				}
			}
			cout<<"Case #"<<c<<": "<<o<<endl;
		}
		c++;
	}
	return 0;
}
