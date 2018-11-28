#include <iostream>
#include <set>
#include <fstream>

using namespace std;
typedef long long ll;
void add_digits(ll n, set<ll> &s)
{
	while (n > 0)
	{
		s.insert(n % 10);
		n /= 10;
	}
}

int main()
{
	//ifstream cin("input.txt");
	//ofstream cout("output.txt");
	int t;
	ll n;
	cin >> t;

	for (int i = 1; i <= t; ++i)
	{
		cin >> n;

		if (n == 0)
		{
			cout << "Case #" << i << ": INSOMNIA" << endl;
			continue;
		}

		set<ll> s;
		ll ii = -1;
		while (s.size() < 10)
		{
			add_digits(n * ++ii, s);
		}
		cout << "Case #" << i << ": " << n * ii << endl;
	}
	return 0;
}