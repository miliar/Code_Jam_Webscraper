#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

vector <unsigned long long> a;

unsigned long long gcd(unsigned long long a, unsigned long long b)
{
	unsigned long long r;
	while(b!=0)
	{
		r=b;
		b=a%b;
		a=r;
	}
	return a;
}

unsigned long long p,q,s;

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	for(unsigned long long i=1;i<1001000000000;i*=2)
	{
		a.push_back(i);
	}
	cin>>s;
	for(int g=0;g<s;g++)
	{
		bool chk=false;
		scanf("%64d/%64d",&p,&q);
		cout<<"Case #"<<g+1<<": ";
		unsigned long long r=gcd(q,p);
		p/=r;
		q/=r;
		int xar;
		for(int i=0;i<a.size();i++)
		{
			if(q==a[i])
			{
				chk=true;
				break;
			}
		}
		if(!chk)
		{
			cout<<"impossible"<<endl;
			continue;
		}
		double k=((double)q)/p;
		for(int i=0;i<a.size();i++)
		{
			if(a[i]>=k)
			{
				cout<<i<<endl;
				break;
			}
		}
	}
	return 0;
}
