
#include <iostream>

using namespace std;

typedef unsigned int uint;
typedef unsigned long long ull;

inline uint log2_bound_32(uint x)
{
	uint r = 0;
	if (x >= 65536)
	{
		x >>= 16;
		r += 16;
	}
	if (x >= 256)
	{
		x >>= 8;
		r += 8;
	}
	if (x >= 16)
	{
		x >>= 4;
		r += 4;
	}
	if (x >= 4)
	{
		x >>= 2;
		r += 2;
	}
	if (x >= 2)
	{
		x >>= 1;
		r += 1;
	}
	return r + x;
}

inline uint BitLen(uint x)
{
	return log2_bound_32(x);
}

inline uint BitLen(ull x)
{
	uint h = x >> 32;
	return h ? 32 + log2_bound_32(h) : log2_bound_32(uint(x));
}

ull GetRepr(uint x, uint base)
{
	ull ret = 0;

	ull basePow = 1;
	for (; x; x >>= 1, basePow *= base)
	{
		ret += (x & 1) * basePow;
	}

	return ret;
}

ull GetDivisor(ull x)
{
	ull lim = 1<<(BitLen(x)/2);
	for (ull d = 2; d < lim; ++d)
	{
		if (x % d == 0)
		{
			return d;
		}
	}

	return 0; //no divisor -> prime
}

void PrintCoin(uint c, uint nbit)
{
	for (int bmask=1<<(nbit-1); bmask; bmask>>=1)
	{
		cout << ((c & bmask) ? 1 : 0);
	}
}


int main()
{
	const int D = 10;
#if 1
	int N = 16;
	int J = 50;
#else
	int N = 6;
	int J = 3;
#endif

	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		cout << "Case #" << i << ":" << endl;

		cin >> N >> J;

		int j = 0;

		uint coinBits = (1 << (N - 1)) + 1;
		uint coinBitsEnd = 1 << N;
		for (; coinBits < coinBitsEnd; coinBits += 2)
		{
			ull divisors[D + 1];
			bool bFoundPrime = false;
			for (uint b = 2; b <= D && !bFoundPrime; ++b)
			{
				ull nBase = GetRepr(coinBits, b);
				divisors[b] = GetDivisor(nBase);
				if (divisors[b] == 0)
				{
					bFoundPrime = true;
				}
			}
			if (!bFoundPrime)
			{
				PrintCoin(coinBits, N);
				for (uint b = 2; b <= D; ++b)
				{
					cout << " " << divisors[b];
				}
				cout << endl;

				if (++j == J)
					break;
			}
		}
	}

	return 0;
}
