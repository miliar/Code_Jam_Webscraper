#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>

using namespace std;

using ull = unsigned long long;

ull findDiv(ull val)
{
	ull last = sqrt(val);
	for (ull i = 2; i <= last; ++i) if (val % i == 0) return i;
	return 1;
}

ull lpow(ull n, ull p)
{
	ull res = 1;
	for (ull i = 0; i < p; ++i) res *= n;
	return res;
}

bool isPrime(ull n)
{
	ull end = sqrt(n);
	for (ull i = 2; i <= end; ++i) if (n % i == 0) return false;
	return true;
}

int main(int argc, char** argv)
{
	ifstream in(argv[1]);
	ofstream out(argv[2]);
	if (in.is_open() && out.is_open())
	{
		int ts; in >> ts;
		for (int t = 1; t <= ts; ++t)
		{
			out << "Case #" << t << ":\n";
			int n, j; in >> n >> j;
			ull mx = (1 << (n - 1)) + 1;
			ull end = lpow(2, (n - 2));
			for (ull i = 0; j > 0 && i < end; ++i)
			{
				ull cur = (i << 1) | mx;
				bool ok = true;
				vector<ull> vals;
				for (ull base = 2; ok && base <= 10; ++base)
				{
					ull val = 0;
					ull tmp = cur;
					ull pw = 0;
					while (tmp > 0)
					{
						val += ((tmp & 1) * lpow(base, pw));
						++pw;
						tmp >>= 1;
					}
					if (isPrime(val)) ok = false;
					vals.push_back(val);
				}
				if (ok)
				{
					out << vals.back();
					for (const auto& val : vals) out << " " << findDiv(val);
					out << '\n';
					--j;
				}
			}
		}
	}
	else
	{
		cerr << "failed to open file\n";
	}
	return 0;
}
