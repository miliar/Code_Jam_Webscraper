#include <iostream>
#include <cstdint>

using namespace std;

static uint64_t N, J;

uint64_t jamcoin;
uint64_t divisors[11];

uint64_t LIMIT;
uint64_t MAX[11] = {0,1,2,3,4,5,6,7,8,9,10};

inline bool is_divisible(uint64_t divisor, int base)
{
	uint64_t digit_value = 1;
	uint64_t remainder = 0;

	for (int i = 0; i < N; ++i)
	{
		remainder = (remainder + digit_value * ((jamcoin >> i) & 1)) % divisor;
		digit_value = (digit_value * base) % divisor;
	}

	return (remainder == 0);
}

inline int find_divisor(int base)
{
	for (uint64_t divisor = 2; divisor <= MAX[base]; ++divisor)
	{
		if (is_divisible(divisor, base)) return divisor;
	}
	return 0;
}

void print_answer()
{
	for (int i = 0; i < N; ++i)
	{
		cout << ((jamcoin >> (N-i-1)) & 1);
	}

	for (int base = 2; base <= 10; ++base)
	{
		cout << ' ' << divisors[base];
	}

	cout << endl;
}

int main()
{
	int ncases;
	cin >> ncases;
	if (ncases != 1) return -1;

	cin >> N >> J;

	for (int i = 0; i < N / 8; ++i)
	{
		for (int base = 2; base <= 10; ++base)
		{
			MAX[base] *= base;
		}
	}

	cout << "Case #1:" << endl;

	LIMIT = 1l << N;
	int nsuccess = 0;

	for (jamcoin = (1l << (N-1)) + 1l; jamcoin < LIMIT && nsuccess < J; jamcoin += 2)
	{
		bool success = true;
		for (int base = 2; base <= 10; ++base)
		{
			divisors[base] = find_divisor(base);
			if (divisors[base] == 0)
			{
				success = false;
				break;
			}
		}

		if (success)
		{
			++nsuccess;
			print_answer();
		}
	}

	if (nsuccess < J)
	{
		cerr << "FAILED!!!" << endl;
	}
}