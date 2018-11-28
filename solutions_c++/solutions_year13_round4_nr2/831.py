#include<iostream>
using namespace std;

int main()
{
	long long t, a, b, p, ap, s, n, k;
	cin>>t;
	for(int q=1; q<=t; q++)
	{
		cin>>n>>p;
		p--;
		a=0;
		b=(1<<n)-1;
		while(a!=b)
		{
			s=(a+b+1)/2;
			k=s;
			ap=0;
			for(int i=0; i<n; i++)
			{
				ap*=2;
				if(k)
				{
					k--;
					k/=2;
					ap++;
				}
			}
			if(ap>p)
			{
				b=s-1;
			}
			else
			a=s;
		}
		cout<<"Case #"<<q<<": "<<a<<" ";
		a=0;
		b=(1<<n)-1;
		while(a!=b)
		{
			s=(a+b+1)/2;
			k=(1<<n)-s-1;
			ap=0;
			for(int i=0; i<n; i++)
			{
				ap*=2;
				if(k)
				{
					k--;
					k/=2;
				}
				else
				{
					ap++;
				}
				//cout<<i<<" "<<s<<" "<<ap<<"\n";
			}
			if(ap>p)
			{
				b=s-1;
			}
			else
			a=s;
		}
		cout<<a<<"\n";
	}
	return 0;
}
