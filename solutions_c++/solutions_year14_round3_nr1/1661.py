#include <iostream>
#include <cmath>

using namespace std;

long long gcd(long long a, long long b)
{
	long long c = a % b;

	if (c == 0)
		return b;

	return gcd(b, c);
}

int main()
{
	int cases;

	std::cin >> cases;

	for (int c = 1; c <= cases; c++) {
		long long p, q;
		char temp;

		cin >> p >> temp >> q;

		long long g = gcd(p, q);

		if (g != 1) {
			p /= g;
			q /= g;
		}

		int k = (int)log2(q);
		int m = 1 << k;

		if (m != q)
			cout << "Case #" << c << ": impossible" << endl;
		else {
			int generation = 0;

			do {
				p <<= 1;
				generation++;
			} while (p < q);

			if (generation > 40)
				cout << "Case #" << c << ": impossible" << endl;
			else
				cout << "Case #" << c << ": " << generation << endl;
		}
	}

	return 0;
}
