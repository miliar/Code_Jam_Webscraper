#include<fstream>
#include<cmath>
using namespace std;
int palin(long long n)
{
	long long m=n;
	long long a=0;
	int x;
	while(n>0)
	{
		x=n%10;
		n=n/10;
		a=a*10+x;
	}
	if(m==a)
		return 1;
	return 0;
}
int psqr(long long a)
{
	double d;
	d=double(a);
	d=sqrt(d);
	long long b=d;
	if(b*b==a)
	{	
		if(palin(b)==1)
			return 1;
	}
	return 0;
}
int main()
{
	ifstream f("C-small-attempt0.in");
	ofstream f1("output.txt");
	int t=0;
	long long a,b,c=0;
	f>>t;
	for(int k=0;k<t;k++)
	{
		c=0;
		f>>a>>b;
		for(long long i=a;i<=b;i++)
		{
			if(palin(i)==1)
			{
				if(psqr(i)==1)
				{
					c++;
				}
			}
		}
		f1<<"Case #"<<k+1<<": "<<c<<endl;
	}
	return 0;
}