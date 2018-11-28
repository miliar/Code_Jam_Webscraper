
#define PROBLEM_NAME "C"
#define PROBLEM_SMALL_INPUT "-small-attempt0"
#define PROBLEM_LARGE_INPUT "-large"

#include <set>
#include <vector>

using namespace std;

class Jamcoin
{
public:
	vector<int> val;
	__int64 count;
	__int64 maxcount;
	Jamcoin(int n)
	{
		val.push_back(1);
		for (int i=1; i<n-1; ++i)
		{
			val.push_back(0);
		}
		val.push_back(1);
		count = 0;
		maxcount = (__int64) pow((double)2, (double)n-2);
	}

	bool next()
	{
		if (count + 1 >= maxcount)
			return false;

		count++;
		++val[val.size()-2];
		for (int i = (int) val.size()-2; i >= 1; --i)
		{
			if (val[i] > 1)
			{
				val[i] = 0;
				if (i >= 2)
					++val[i-1];
			}
		}
		return true;
	}

	__int64 eval(int base)
	{
		__int64 rval = 0;
		__int64 mul = 1;

		for (int i = (int) val.size()-1; i >= 0; --i)
		{
			rval += mul * val[i];
			mul *= base;
		}
		return rval;
	}

	void print()
	{
		for (size_t i=0; i<val.size(); ++i)
		{
			fout << val[i];
		}
	}
};


vector<__int64> primes;

__int64 primality(__int64 num)
{
	__int64 maxval = (__int64) sqrt((double) num) + 1;
	for (size_t i=0; i<primes.size(); ++i)
	{
		if (num == primes[i])
			return 0;

		__int64 remainder = num % primes[i];
		if (remainder == 0)
			return primes[i]; // not prime
	}
	return 0; // prime
}

int main(int argc, char* argv[])
{
//	set_fio(PROBLEM_NAME ".txt");
//	set_fio(PROBLEM_NAME PROBLEM_SMALL_INPUT ".in");
	set_fio(PROBLEM_NAME PROBLEM_SMALL_INPUT ".in", PROBLEM_NAME PROBLEM_SMALL_INPUT ".out.txt");
//	set_fio(PROBLEM_NAME PROBLEM_LARGE_INPUT ".in");
//	set_fio(PROBLEM_NAME PROBLEM_LARGE_INPUT ".in", PROBLEM_NAME PROBLEM_LARGE_INPUT ".out.txt");

	{
		primes.reserve(1000100);
		ifstream ifs_prime;
		ifs_prime.open("50M_part1.txt");
		while(!ifs_prime.eof())
		{
			__int64 p;
			ifs_prime >> p;
			primes.push_back(p);
		}
	}

	int T;
	fin >> T;
	for (int cases=1; cases<=T; ++cases)
	{
		int N, J;
		fin >> N >> J;

		fout << "Case #" << cases << ":" << endl;

		Jamcoin coin(N);
		int j = 0;

		//int ii = 0;
		//do
		//{
		//	fout << (ii++) << " : ";
		//	coin.print();
		//	fout << endl;
		//} while (coin.next());

		//if(false)
		do
		{
			bool valid = true;
			vector<__int64> evals;
			vector<__int64> divisors;
			for (int base = 2; base <= 10; ++base)
			{
				__int64 val = coin.eval(base);
				__int64 divisor = primality(val);

				if (divisor == 0)
				{
					valid = false;
					break;
				}
				evals.push_back(val);
				divisors.push_back(divisor);
			}
			if (valid)
			{
				coin.print();
				for (size_t i=0; i<divisors.size(); ++i)
				{
					//fout << " " << evals[i] << "(by " << divisors[i] << ")";
					fout << " " << divisors[i];
				}
				fout << endl;
				++j;
			}
		}
		while (coin.next() && j < J);
		//while (coin.next());
	}

	return 0;
}
