#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <limits>
#include <cassert>
#include <cmath>
#include <algorithm>
#include <iterator>
#include <map>

using namespace std;

typedef unsigned long long ull;
typedef map<ull, vector<ull>> NumToPowersMap;
NumToPowersMap numToPowersMap;

size_t N, J;

void precomputeNumToPowersMap()
{
	for (ull i = 2; i <= 10; i++)
	{
		vector<ull>& powers = numToPowersMap[i];
		powers.push_back(1);
		ull currentPower = i;
		for (ull j = 1; j < J; j++)
		{
			powers.push_back(currentPower);
			currentPower *= i;
		}
	}
}

ull checkPrime(ull num)
{
	for (ull i = 2; i < num; i++)
	{
		if (num % i == 0) return i;
		ull quotient = ceil(num / i);
		if (i > quotient) break;
	}
	return 1;
}

ull getNumForBase(ull binary, ull base)
{
	vector<ull>& powers = numToPowersMap[base];
	ull num = powers[0] + powers[J-1];
	for (ull i = 1; i <= J-2; i++)
	{
		ull bit = binary & 1;
		binary >>= 1;
		if (!bit) continue;
		num += powers[i];
	}
	return num;
}

string getBinaryString(ull i)
{
	string binaryString = "1";
	for (size_t j = 0; j < J-2; j++)
	{
		binaryString += (i & 1 ? "1" : "0");
		i >>= 1;
	}
	binaryString += "1";
	reverse(binaryString.begin(), binaryString.end());
	return binaryString;
}

void printResult(ull i, vector<ull>& divisors)
{
	string numStr = getBinaryString(i);
	cout << numStr;
	for (size_t i = 0; i < divisors.size(); i++)
		cout << " " << divisors[i];
	cout << endl;
}

void printResult()
{
	ull numResults = 0;
	ull limit = pow(2,J-2);
	for (ull i = 0; i <= limit; i++)
	{
		vector<ull> divisors;
		for (ull j = 2; j <= 10; j++)
		{
			ull num = getNumForBase(i, j);
			ull divisor = checkPrime(num);
			if (divisor == 1) break;
			divisors.push_back(divisor);
		}
		if (divisors.size() == 9)
		{
			printResult(i, divisors);
			numResults++;
			if (numResults == N) return;
		}
	}
}

int main(int argc, char** argv)
{
	ifstream input(argv[1]);
  ull T;
  input >> T;

  for (ull i = 1; i <= T; i++)
	{
		input >> J >> N;

		precomputeNumToPowersMap();

		cout << "Case #" << i << ":" << endl;
		printResult();
	}

  return 0;
}
