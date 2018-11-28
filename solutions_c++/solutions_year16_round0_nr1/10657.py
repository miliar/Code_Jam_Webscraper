#include <iostream>
using namespace std;
int a[10];
void split(long int s)
{
	long int x=s;
	while (x!=0)
	{
		a[x%10]=x%10;
		x=x/10;
	}
}
bool check()
{
	for (int i=0;i<10;i++)
	{
		if (a[i]==-1)
			return false;
	}
	return true;
}
int main()
{
	int t;
	cin>>t;
	for (int test=0;test<t;test++)
	{
		long int n;
		cin>>n;
		long int f=n;
		bool s=false;
		if (n==0)
			cout<<"Case #"<<test+1<<": "<<"INSOMNIA"<<"\n";
		else
		{
			for (int i=0;i<10;i++)
			{
				a[i]=-1;
			}
			while (s==false)
			{
				split(n);
				s=check();
				n=n+f;
			}
		}
		if (s==true)
		{
			cout<<"Case #"<<test+1<<": "<<n-f<<"\n";
		}
	}
}
