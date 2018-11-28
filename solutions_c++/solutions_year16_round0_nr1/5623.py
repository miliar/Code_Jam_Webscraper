#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <set>

using namespace std;

typedef long long lol;

int T;

long long interpreta(long long jam, long long base)
{
	long long res = 0;
	long long a = 2;
	while(a<jam)
		a*=10;
	a/=2;
	while(a!=0)
	{
		res *= base;
		res += (jam/a)%10;
		a /= 10;
	}
	/*while(jam!=0)
	{
		res *= base;
		res += jam%10;
		jam /= 10;
	}*/
	return res;
}

long long pow(long long a, long long b)
{
	if(b==0)
		return 1;
	if(b==1)
		return a;
	long long res = pow(a,b/2);
	res *= res;
	if(b%2)
		res *= a;
	return res;
}

long long calculajam(long long n,long long asdf)
{
	long long res = 1;
	for(int i=0;i<n-2;i++)
	{
		res*=10;
		res += asdf&1;
		asdf /= 2;
	}
	res *=10;
	res++;
	return res;
}

void func2(lol n, vector<int>& v)
{
	while(n!=0)
	{
		v[n%10]++;
		n/=10;
	}
}

lol func(lol n)
{
	vector<int> v(10);
	lol i=1;
	while(true)
	{
		func2(i*n,v);
		for(int j=0;j<10;j++)
		{
			if(!v[j])
				goto aaa;
		}
		return i*n;
		aaa:;
		i++;
	}
}

int main()
{
	cin >> T;
	for(int I=0;I<T;I++)
	{
		lol n;
		cin >> n;
		cout << "Case #" << I+1 << ": ";
		if(!n)
			cout << "INSOMNIA" << endl;
		else
		 	cout << func(n) << endl;
		
	}
}
