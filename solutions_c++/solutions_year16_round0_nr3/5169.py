#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

unsigned long long divisors[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263};

unsigned long long reinterpret(unsigned long long n, int base)
{
	unsigned long long ret = 0;
	unsigned long long b = 1;
	while (n > 0)
	{
		ret += b * (n & 1);
		b *= base;
		n = n >> 1;
	}
	return ret;
}

void base2(unsigned long long n)
{
	string s;
	while (n > 0)
	{
		s.push_back('0' + (n&1));
		n = n >> 1;
	}
	reverse(s.begin(), s.end());
	cout << s;
	
}

unsigned long long isdivisible(unsigned long long n)
{
	for (unsigned int i = 0; i < sizeof(divisors)/sizeof(divisors[0]); ++i)
	{
		if (((n % divisors[i]) == 0) && (n != divisors[i]))
		{
			return divisors[i];
		}
	}
	return 0;
}

int main(int argc, char **argv)
{
	int cases, N,J;
	cin >> cases >> N >> J;
	cout << "Case #1:\n";
	unsigned long long base = 1 + ((unsigned long long) 1 << (N-1));
	for (int i = 0; i < J; /* only increment in positive case */)
	{
		vector<int> divisors;
		for (int j = 2; j <= 10; ++j)
		{
			unsigned long long n = reinterpret(base, j);
			unsigned long long divisor = isdivisible(n);
			if (divisor == 0) break;
			cerr << "divisor(" << base << "," << j << "," << n << "): " << divisor << endl;
			divisors.push_back(divisor);
		}
		if (divisors.size() == 9)
		{
			base2(base);
			for (int j = 0; j < 9; ++j)
			{
				cout << " " << divisors[j];
			}
			cout << "\n";
			++i;
		}
		base += 2; // keep the 1 at the end
		if ((base & (1 << (N-1))) == 0) cerr << "ARGH!\n";
		if ((base & (1 << (N-1))) == 0) return 0;
	}
}
