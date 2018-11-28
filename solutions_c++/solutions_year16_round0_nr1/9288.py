#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>
#include <string>
#include <set>
using namespace std;
typedef long long ll;
set<int> s;


bool f(ll k)
{
	while (k)
	{
		if (s.count(k%10))
			s.erase(k%10);
		k/=10;
	}
	return s.size()==0;
}

int main()
{
    //ios::sync_with_stdio(false);
    freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin >> t;

	for (int tt = 0; tt<t; tt++)
	{
		bool ok = false;
		ll n;
		for (int i = 0; i<10; i++)
			s.insert(i);

		cin >> n;
		ll i =1;
		for (; i<10000; i++)
		{
			if (ok = f(i*n))
				break;
		}
		cout << "Case #"<<tt+1<< ": ";
		if (ok)
			cout << i*n;
		else
			cout << "INSOMNIA";
		cout << endl;
	}
	return 0;   
}									  