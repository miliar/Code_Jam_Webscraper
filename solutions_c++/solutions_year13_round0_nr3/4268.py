#include <algorithm>
#include <fstream>
#include <iostream>
#include <iterator>
#include <map>
#include <math.h>
#include <set>
#include <stack>
#include <string>
#include <vector>

// Boost 1.53
#include <boost/algorithm/string.hpp>
#include <boost/lexical_cast.hpp>
#include <boost/range/adaptor/reversed.hpp>
#include <boost/range/algorithm.hpp>

//#define VERBOSE

//const std::string FILE_NAME = "test";
//const std::string FILE_NAME = "C-small-attempt0";
const std::string FILE_NAME = "C-large-1";
const std::string FILE_NAME_IN = FILE_NAME + ".in";
const std::string FILE_NAME_OUT = FILE_NAME + ".out";

struct TestCase
{
	size_t start;
	size_t end;

	std::string execute() const;
};

void executeTests(const std::vector<TestCase>& testCases);
std::vector<TestCase> readTestCases();

int main()
{
	auto tests = readTestCases();
	executeTests(tests);

	return 0;
}

void executeTest(const TestCase& test, std::ofstream& fout, size_t total)
{
	static int number = 1;
	static double lastPer = 0;

#ifdef VERBOSE
	std::cout << "Executing test case " << number << ": ";
#endif

	auto result = test.execute();

#ifdef VERBOSE
	std::cout << result << std::endl;
#endif

	fout << "Case #" << number << ": " << result << std::endl;

	double per = number * 100.0 / total;

	if (per >= lastPer + 1)
	{
		std::cout << static_cast<int>(per) << "% complete\n";
		lastPer = per;
	}

	number++;
}

void executeTests(const std::vector<TestCase>& tests)
{
	std::ofstream fout(FILE_NAME_OUT);
	auto count = tests.size();
	boost::for_each(tests, [&](const TestCase& test) { executeTest(test, fout, count); });
	fout.flush();
	fout.close();
}

TestCase readTestCase(std::ifstream& fin)
{
	TestCase test;

	fin >> test.start >> test.end;

	return test;
}

std::vector<TestCase> readTestCases()
{
	std::vector<TestCase> cases;
	std::ifstream fin(FILE_NAME_IN);

	int caseCount = 0;
	fin >> caseCount;
	std::cout << "Reading in " << caseCount << " test cases.\n";

	std::generate_n(std::back_inserter(cases), caseCount, [&] { return readTestCase(fin); });
	
	fin.close();

	return cases;
}

bool isPalendrome(size_t num)
{
	auto numStr = boost::lexical_cast<std::string>(num);
	auto numRevStr = numStr;

	boost::trim_left_if(boost::reverse(numRevStr), boost::is_any_of("0"));

	return numStr == numRevStr;
}

std::string TestCase::execute() const
{
	static std::set<size_t> fairAndSquare;
	static size_t maxEnd = 0;


	if (this->end > maxEnd)
	{
		auto startF = sqrt(static_cast<long double>(maxEnd));
		auto start = static_cast<size_t>(floor(startF));
		
		auto endF = sqrt(static_cast<long double>(this->end));
		auto end = static_cast<size_t>(ceil(endF));

		for (auto i = start; i <= end; i++)
		{
			if (isPalendrome(i))
			{
				auto i2 = i * i;
			    if (isPalendrome(i2))
					fairAndSquare.insert(i2);
			}
		}

		maxEnd = this->end;
	}

	size_t count = boost::count_if(fairAndSquare, [this](size_t val) { return val >= start && val <= end; });

	return boost::lexical_cast<std::string>(count);
}
