#include "stdafx.h"

void go(int caseN);

vector<uint32_t> primes;
void make_some_primes()
{
	primes.reserve(9592);
	primes.push_back(2);
	for (uint32_t i = 3; i <= 100000; i += 2)
	{
		if (none_of(primes.begin(), primes.end(), [&](uint32_t p) { return i % p == 0; }))
		{
			primes.push_back(i);
		}

	}
}

int main()
{
	ifstream in("C-small-attempt0.in");
	ofstream out("out.txt");
	cin.rdbuf(in.rdbuf());
	cout.rdbuf(out.rdbuf());

	make_some_primes();

	int T; 
	cin >> T;
	for (int t = 1; t <= T; ++t) go(t);
    return 0;
}


void go(int caseN)
{
	cout << "Case #" << caseN << ":" << endl;

	int N, J;
	cin >> N >> J;

	for (int x = (1 << (N - 1)) + 1; J > 0; x += 2)
	{
		uint64_t base[9] = {};
		uint64_t m[9] = { 1, 1, 1, 1, 1, 1, 1, 1, 1 };
		int test = x;
		for (int i = 0; i < N; ++i)
		{
			for (int k = 0; k < 9; ++k)
			{
				if (test & 1)
				{
					base[k] += m[k];
				}
				m[k] *= k + 2;
			}
			test >>= 1;
		}

		uint32_t divs[9] = {};
		int found = 0;
		int maxDiv = sqrt(x);
		for (int i = 0; i < primes.size(); ++i)
		{
			uint32_t& div = primes[i];
			if (div > maxDiv) break;
			for (int k = 0; k < 9; ++k)
			{
				if (divs[k] == 0 && (base[k] % div) == 0) { ++found; divs[k] = div; }
			}
			if (found == 9)
			{
				--J;
				cout << bitset<16>(x);
				for (int k = 0; k < 9; ++k) cout << " " << divs[k];				
				cout << endl;
				break;
			}
		}
	}
}

