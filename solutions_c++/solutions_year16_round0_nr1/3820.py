#include <iostream>

using namespace std;

long int counts(int n,long int q,long int ar[10])
{
	long int p=q;
	while(p)
	{
		ar[p%10]++;
		p=p/10;
	}
	for (int i = 0; i < 10; i++)
	{
		if (!ar[i])
		{
			return counts(n,q+n,ar);
		}
	}
	return q;
}

int main()
{
	int t;
	cin>>t;
	for (int i = 0; i < t; i++)
	{
		int n;
		cin>>n;
		if (!n)
		{
			cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
			continue;
		}
		else
		{
			long int ar[10]={0};
			long int an=counts(n,n,ar);
			cout<<"Case #"<<i+1<<": "<<an<<endl;

		}
	}
	return 0;
}