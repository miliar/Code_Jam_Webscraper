#include<cstdio>
#include<iostream>
#include<bitset>
using namespace std;
typedef long long ll;

bitset<10> b;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d\n", &t);
	for (int q = 0; q < t; q++)
	{
		ll n;
		cin >> n;
		b.reset();
		int iter = 0;
		ll x = 1;
		while (b.count() != 10 && iter <= 1000000)
		{
			ll d = n * x;
			while (d > 0)
			{
				b[d % 10] = 1;
				d /= 10;
			}
			x++;
			iter++;
		}
		x--;
		cout << "Case #" << (q + 1) << ": ";
		if (b.count() != 10)
			cout << "INSOMNIA\n";
		else
			cout << n * x << "\n";
	}
	return 0;
}