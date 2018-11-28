#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

long long convertBase(vector<long long> src, long long b)
{
	long long ret = 0;
	long long len = src.size();
	long long factor = 1;

	for (long long i = len - 1; i >= 0; --i)
	{
		ret += factor * src[i];
		factor *= b;
	}

	return ret;
}

bool isPrime(long long num)
{
	if (num <= 1)
		return false;
	else if (num == 2)
		return true;
	else if (num % 2 == 0)
		return false;
	else
	{
		bool prime = true;
		long long divisor = 3;
		double num_d = static_cast<double>(num);
		long long upperLimit = static_cast<long long>(sqrt(num_d) + 1);

		while (divisor <= upperLimit)
		{
			if (num % divisor == 0)
				prime = false;
			divisor += 2;
		}
		return prime;
	}
}

vector<long long> getRepresentation(long long N)
{
	vector<long long> ret;
	while (N)
	{
		ret.insert(ret.begin(), N % 2);
		N = N / 2;
	}

	return ret;
}

void printRepresentation(vector<long long> num)
{
	for (auto i : num)
	{
		cout << i;
	}
}

long long findFactor(long long N)
{
	for (long long i = 2; i < N; i++)
	{
		if (N % i == 0)
		{
			return i;
		}
	}

	return -1;
}

bool checkNum(vector<long long> num)
{
	for (long long b = 2; b <= 10; ++b)
	{
		if (isPrime(convertBase(num, b)))
		{
			return false;
		}
	}
	return true;
}

int main()
{
	long long T;
	cin >> T;

	for (long long t = 1; t <= T; ++t)
	{
		long long N, J;
		cin >> N;
		cin >> J;

		long long from = ((long long)1 << (N - 1)) + 1;
		long long to = ((long long)1 << N) - 1;
		long long count = 0;

		cout << "Case #" << t << ":" << endl;
		for (long long n = from; n <= to; n += 2)
		{
			vector<long long> rep = getRepresentation(n);
			if (checkNum(rep))
			{
				count++;
				printRepresentation(rep);
				for (long long b = 2; b <= 10; ++b)
				{
					cout << " " << findFactor(convertBase(rep, b));
				}
				cout << endl;
			}

			if (count == J)
			{
				break;
			}
		}

	}


	return 0;

}