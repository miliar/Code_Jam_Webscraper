#include <bits/stdc++.h>

using namespace std;
typedef unsigned long long ull;

int uzupelnij(ull x, vector < ull >& V)
{
	while(x > 0)
	{
		V[x%10] ++;
		x/=10;
	}
	for(auto el: V)
		if (el == 0)
			return true;
	return false;
}

ull test()
{
	vector < ull > V(10, 0);
	ull x;
	cin>>x;
	if (x == 0)
		return -1;
	ull z = x;
	while(uzupelnij(z, V))
	{
		z+=x;
	}
	return z;
}

int main()
{
	int testy;
	cin>>testy;
	for(int i=1; i<=testy; i++)
	{
		ull pom = test();
		if (pom == -1)
			cout << "Case #"<<i<<": "<<"INSOMNIA"<<"\n";
		else
			cout << "Case #"<<i<<": "<<pom<<"\n";
	}
}

