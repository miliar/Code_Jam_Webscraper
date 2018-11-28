#include <iostream>
#include <fstream>
#include <string>
#include <vector>

unsigned long long GetValue(const std::vector<bool> &Digits, const unsigned int Base)
{
	unsigned long long Result = 0;

	unsigned long long Column = 1;
	for (unsigned int x = Digits.size() - 1; x < Digits.size(); x--)
	{
		if (Digits[x])
			Result += Column;
		Column *= Base;
	}

	return Result;
}

unsigned long long GetPrimeFactor(const unsigned long long Value, std::vector<unsigned long long> &Primes)
{
	unsigned long long Root = (unsigned long long)sqrt(Value);

	// Check for prime factors already calculated
	for (unsigned int x = 0; x < Primes.size() && Primes[x] <= Root; x++)
	{
		if (Value % Primes[x] == 0)
			return Primes[x];
	}

	// Generate new primes and check
	unsigned long long Counter = Primes[Primes.size() - 1];
	while (Counter <= Root && Counter <= 1000000)
	{
		Counter += 2;

		bool Prime = true;
		for (unsigned int x = 0; x < Primes.size(); x++)
		{
			if (Counter % Primes[x] == 0)
			{
				Prime = false;
				break;
			}
		}
		if (Prime)
		{
			Primes.push_back(Counter);
			if (Value % Counter == 0)
				return Counter;
		}
	}

	// Prime
	return -1;
}

void Increment(std::vector<bool> &Pattern)
{
	for (unsigned int x = Pattern.size() - 2; x > 0; x--)
	{
		if (!Pattern[x])
		{
			Pattern[x] = true;
			return;
		}
		else
			Pattern[x] = false;
	}

	throw std::exception("Overflowed");
}

class Result
{
public:
	std::vector<bool> Pattern;
	std::vector<unsigned long long> Factors;

	Result()
	{

	}
	Result(const std::vector<bool> Pattern, const std::vector<unsigned long long> Factors)
	{
		this->Pattern = Pattern;
		this->Factors = Factors;
	}
};

std::string GetString(const std::vector<bool> &Digits)
{
	std::vector<char> Result;
	Result.resize(Digits.size());

	for (unsigned int x = 0; x < Digits.size(); x++)
		Result[x] = Digits[x] ? '1' : '0';

	return std::string(Result.begin(), Result.end());
}

int main(int argc, char *argv[])
{
	std::ifstream In("In.txt");
	std::ofstream Out("Out.txt");

	unsigned int T;
	In >> T;

	for (unsigned int t = 0; t < T; t++)
	{
		unsigned int _Digits, Count;
		In >> _Digits >> Count;

		std::vector<bool> Working;
		Working.resize(_Digits, false);
		Working[0] = true;
		Working[Working.size() - 1] = true;

		std::vector<unsigned long long> Primes{ 2, 3 };
		std::vector<Result> Results;
		while (Results.size() < Count)
		{
			std::vector<unsigned long long> Factors;
			Factors.reserve(9);
			for (unsigned int b = 2; b <= 10; b++)
			{
				unsigned long long Value = GetValue(Working, b);
				unsigned long long Factor = GetPrimeFactor(Value, Primes);
				if (Factor != -1)
					Factors.push_back(Factor);
				else
					break;
			}
			if (Factors.size() == 9)
				Results.push_back(Result(Working, Factors));

			if (Results.size() != Count)
				Increment(Working);
		}

		Out << "Case #" << t + 1 << ":" << std::endl;
		for (unsigned int x = 0; x < Results.size(); x++)
		{
			Out << GetString(Results[x].Pattern);
			for (unsigned int y = 0; y < Results[x].Factors.size(); y++)
				Out << " " << Results[x].Factors[y];
			Out << std::endl;
		}
	}

	In.close();
	Out.close();

	return 0;
}