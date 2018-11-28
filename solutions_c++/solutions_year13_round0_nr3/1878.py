#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long ll;

vector<ll> p;
typedef vector<ll>::iterator iter;

bool test(ll num)
{
	char buf[30];

	sprintf(buf, "%I64d", num);

	int n = strlen(buf);

	for (int i=0; i<n/2; ++i)
	{
		if (buf[i] != buf[n-i-1])
			return false;
	}

	return true;
}

void pregen()
{
	for (ll i=1;i<=10000000;++i)
	{
		if (test(i) && test(i*i))
		{
			p.push_back(i*i);
		}
	}
}

int main()
{
	pregen();

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;

	cin >> t;

	for (int i=0; i<t; ++i)
	{
		ll a, b;

		cin >> a >> b;

		iter x = lower_bound(p.begin(), p.end(), a);
		iter y = upper_bound(p.begin(), p.end(), b);

		int d = y - x;

		cout << "Case #" << i+1 << ": " << d << endl;
	}

	return 0;
}