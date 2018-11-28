#include <iostream>
#include <string>
#include <cassert>
#include <vector>
#include <fstream>
#include <cstdint>
#include <cmath>
#include <algorithm>
#include <map>
#include <iterator>
#include <numeric>
#include <cmath>

std::ofstream out;

struct Test 
{
	std::string name;
	int n;
};

typedef std::vector<Test> Tests;

Tests readInput(const char* fn)
{
	std::ifstream ifs(fn);
	assert(ifs.is_open());

	size_t nTests;
	ifs >> nTests;

	Tests tests;
	tests.reserve(nTests);

	for (size_t i = 0;i < nTests; ++i)
	{
		Test t;
		ifs >> t.name >> t.n;
		tests.push_back(t);
	}

	return tests;
}

bool isVowel(char c)
{
	return c == 'a' || c ==  'e'|| c ==  'i'|| c ==  'o'|| c == 'u';
}

size_t nValue(const Test &t)
{
	size_t len = t.name.length();
	
	size_t nv = 0;
	size_t last = 0;
	size_t i = 0;
	while (i <= len - t.n)
	{
		size_t j;
		for (j = 0; j < t.n; ++j)
		{
			if (isVowel(t.name[i+j]))
			{
				i += (j + 1);
				break;
			}
		}
		if (j == t.n)
		{
			nv += (i-last + 1)*(len - i - t.n + 1);
			++i;
			last = i;
		}
	}
	/*
	if (nv)
		++nv;
		*/
	return nv;
}


int main(int argc, char *argv[])
{
	assert(argc > 1);

	std::string in = argv[1];

	out.open(in + ".out", std::ios_base::out | std::ios_base::trunc );

	Tests tests = readInput(in.c_str());

	for (int i = 0; i < tests.size(); ++i)
	{
		out << "Case #" << i + 1 << ": " << nValue(tests[i]) << std::endl;
	}


	return 0;
}