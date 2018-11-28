#include <iostream>
#include <vector>

using namespace std;

typedef long long LL;

const int MIN_BASE = 2;
const int MAX_BASE = 10;
const int MIN_DIVISOR = 2;
const int MAX_DIVISOR = 1000;

const int SOLUTION_COUNT = 500;
const int MAGIC_EXPONENT = 31;
const string HEAD_DIGITS = "1000000000000000";

struct jamcoin
{
	string code;
	vector<int> divisors;
};

LL magic_pow(int n, int mod)
{
  LL result = 1;
  for (int k = 0; k < MAGIC_EXPONENT; k++)
    result = (result * n) % mod;
  return result;
}

void check_solution(const string& digits, vector<jamcoin>& solutions)
{
	int div;
	LL value;
	bool divisible;
	vector<int> divisors;
	for (int base = MIN_BASE; base <= MAX_BASE; base++)
	{
		divisible = false;
		value = stoll(digits, 0, base);
		for (div = MIN_DIVISOR; div <= MAX_DIVISOR && !divisible; div++)
		{
			divisible = ((value + magic_pow(base, div)) % div) == 0;
		}
		if (!divisible)
		{
			return;
		}
		divisors.push_back(div - 1);
	}
	jamcoin solution;
	solution.code = HEAD_DIGITS + digits;
	solution.divisors = divisors;
	solutions.push_back(solution);
}

void solve(int index, string& digits, const int solutionCount, vector<jamcoin>& solutions)
{
	if (solutions.size() < solutionCount)
	{
		if (index < digits.size() - 1)
		{
			digits[index] = '0';
			solve(index + 1, digits, solutionCount, solutions);
			digits[index] = '1';
			solve(index + 1, digits, solutionCount, solutions);
		}
		else
		{
			check_solution(digits, solutions);
		}
	}
}

int main()
{
	string digits = "0000000000000001";
	vector<jamcoin> solutions;
	solve(0, digits, SOLUTION_COUNT, solutions);
	
	cout << "Case #1:" << endl;
	for (int k = 0; k < solutions.size(); k++)
	{
		const jamcoin& coin = solutions[k];
		const vector<int>& divisors = coin.divisors;
		cout << coin.code;
		for (int h = 0; h < divisors.size(); h++)
			cout << ' ' << divisors[h];
		
		cout << endl;
	}
	
	return 0;
}