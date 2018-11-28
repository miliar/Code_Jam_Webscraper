// GoogleCodeJam.cpp : Defines the entry point for the console application.
//

#include <vector>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <iomanip>
#include <algorithm>
#include <list>
#include <set>
#include <unordered_set>
#include <utility>
#include <tuple>
#include <limits>
#include <bitset>

using namespace std;

static const bool bConsoleOut = false;

void SolveIt(const vector<unsigned long>& primes, int iRound, fstream& inputFile, ostream& output, ostream& error);

string ReadString(fstream& input, bool bIsEOL = false)
{
	string line;
	if (bIsEOL)
		getline(input, line);
	else
		getline(input, line, ' ');

	return line;
}

int ReadInt(fstream& input, bool bIsEOL = false)
{
	return atoi(ReadString(input, bIsEOL).c_str());
}

double ReadDouble(fstream& input, bool bIsEOL = false)
{
	return atof(ReadString(input, bIsEOL).c_str());
}

unsigned long long int getInBase(bitset<32> bs, int base)
{
	unsigned long long int result = 0;
	for (int i = 0; i < bs.size(); ++i)
	{
		if (bs[i])
			result += pow(base, i);
	}
	return result;
}

vector<unsigned long> generatePrimes()
{
	unsigned long long int iMax = (1 << 10) - 1;
	iMax = getInBase(bitset<32>(iMax), 10);

	std::vector<unsigned long> primes;
	primes.push_back(2);
	for (unsigned long i = 2;; i++)
	{
		bool isprime = true;
		for (unsigned long j = 0; primes[j] * primes[j] <= i; ++j)
		{
			if (i % primes[j] == 0)
			{
				isprime = false;
				break;
			}
		}
		if (isprime)
		{
			//std::cout << i << std::endl;
			primes.push_back(i);
		}
		if (i * i > iMax)
			break;
	}
	return primes;
}

int main(int argc, char* argv[])
{
	//bitset<32> b((1 << 31) - 1);
	//auto x = getInBase(b, 10);

	auto primes = generatePrimes();

	cout << "primes" << endl;

	fstream inputFile;
	fstream outputFile;

	ostream& output = bConsoleOut ? cout : outputFile;
	ostream& error = cerr;
	if (!bConsoleOut)
	{
		outputFile.open("..\\output.txt", ios::out);
		if (!outputFile.is_open())
		{
			cout << "Meh!";
			return 1;
		}
	}

	inputFile.open(argv[1]);

	if (!inputFile.is_open())
	{
		cout << "Meh!";
		return 1;
	}

	string sLine;
	getline(inputFile, sLine);
	int nCases = atoi(sLine.c_str());

	output << std::setprecision(16);

	for (int iCase = 0 ; iCase < nCases; iCase++)
	{
		output << "Case #" << (iCase + 1) << ": ";
		SolveIt(primes, iCase + 1, inputFile, output, error);
	}

	if (!bConsoleOut)
		outputFile.close();

	if (bConsoleOut)
	{
		cout << endl << "Done...";
		cin.get();
	}

	return 0;
}

#undef max

vector<unsigned long long int> doIt(bitset<32> bs, const vector<unsigned long>& primes, unsigned int base, vector<unsigned long long int> prevs)
{
	auto inBase = getInBase(bs, base);
	for (auto prime : primes)
	{
		if (prime * prime > inBase)
			return{};

		if (inBase % prime == 0)
		{
			prevs.push_back(prime);

			if (base < 10)
				return doIt(bs, primes, base + 1, prevs);
			else
			{
				prevs.insert(prevs.begin(), inBase);
				return prevs;
			}
		}
	}

	return {inBase, base};
}

void SolveIt(const vector<unsigned long>& primes, int iCase, fstream& inputFile, ostream& output, ostream& error)
{
	using tpe = unsigned long long int;
	int N, J;
	inputFile >> N;
	inputFile >> J;

	tpe iStart = (1 << (N - 1)) + 1;
	tpe iEnd = 1 << N;

	int nFound = 0;
	output << endl;
	//output << numeric_limits<tpe>::max() << endl;
	//output << numeric_limits<tpe>::digits10 << endl;
	//bitset<32> b(1 << 22);
	//output << getInBase(b, 9) << endl;

	tpe val = iStart;
	for (auto val = iStart; val != iEnd; ++val)
	{
		vector<tpe> vec_results;
		bitset<32> bs(val);
		if (!bs[0])
			continue;

		auto vals = doIt(bs, primes, 2, {});
		if (vals.size() > 5)
		{
			for (auto x : vals)
				output << x << " ";
			output << endl;
			if (++nFound == J)
				return;
		}
	}
	output << "Too bad ... " << nFound << " " << J;
}
