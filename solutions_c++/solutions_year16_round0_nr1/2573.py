#include <bits/stdc++.h>
#define ll long long
#define ull unsigned long long
#define MOD 1000000007
#define INF 999999999
using namespace std;

ll calc(ll number)
{
	set<int>s;
	ll mul = 1;
	ll num = 0;
	while(s.size() < 10)
	{
		//cout << "here" << endl;
		num = mul * number;
		ll temp = num;
		while(temp)
		{
			s.insert(temp % 10);
			temp /= 10;
		}
		mul++;
	}
	return num;
}

int main()
{
	int tc;
	cin >> tc;
	for(int T=1;T<=tc;T++)
	{
		cout << "Case #" << T << ": ";
		ll n;
		cin >> n;
		if(n == 0)
		{
			cout << "INSOMNIA\n";
		}
		else
		{
			cout << calc(n) << "\n";
		}
	}
}
