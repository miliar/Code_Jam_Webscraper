#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	bool check(int n);
	int N=16;
	int J=50;
	int n = 1+(1<<15);
	cout<< "Case #1:" << endl;
	for(;J;n+=2)
	{
		if(check(n))
			J--;
	}
	return 0;
}

bool check(int n)
{
	long long d[11];
	for(int b=2; b<=10; b++)
	{
		long long nb = 0;
		long long o = 1;
		for(int i = n; i; i>>=1)
		{
			if(i&1)
				nb+=o;
			o*=b;
		}
		for(d[b]=2; d[b]*d[b] < nb; d[b]++)
		{
			if(nb%d[b] == 0)
				break;
		}
		if(d[b]*d[b] >= nb)
			return false;
	}
	
	int mask = 1;
	while(mask<=n)
	{
		mask<<=1;
	}
	mask>>=1;
	for(;mask;mask>>=1)
		cout << (n&mask?'1':'0');
	for(int b=2; b<=10; b++)
		cout << ' ' << d[b];
	cout<<endl;
	return true;
}
