#include <iostream>

using namespace std;

uint64_t nod(uint64_t a, uint64_t b);

int main()
{
	int t;
	cin >> t;
	for (int cn = 1; cn <= t; ++cn)
	{
		uint64_t p, q;
		cin >> p;
		char dummy;
		cin.read(&dummy,1);
		cin >> q;

		uint64_t n = nod(p,q);
		p /= n;
		q /= n;

		int c = 0;
		uint64_t d = q;
		while (d > 0)
		{
			c += d&1;
			d >>= 1;
		}
		if (c > 1)
		{
			cout << "Case #" << cn << ": impossible\n";
		}
		else
		{
			int g = 0;
			while (p < q)
			{
				++g;
				q /= 2;
			}
			cout << "Case #" << cn << ": " << g << "\n";
		}
	}

    return 0;
}

uint64_t nod(uint64_t a, uint64_t b)
{
	if (a < b)
	{
		uint64_t t = a;
		a = b;
		b = t;
	}
	while (b > 0)
	{
		a = a%b;
		if (a < b)
		{
			uint64_t t = a;
			a = b;
			b = t;
		}
	}
	return a;
}
