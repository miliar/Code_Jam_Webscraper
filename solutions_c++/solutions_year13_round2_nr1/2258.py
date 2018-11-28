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

std::ofstream out;

typedef std::vector<int> Motes;

struct Field
{
	int player;
	Motes motes;
	int first;
	int last;
};

typedef std::vector<Field> Tests;

Tests readInput(const char* fn)
{
	std::ifstream ifs(fn);
	assert(ifs.is_open());


	size_t nTests;
	ifs >> nTests;

	Tests tests;
	tests.reserve(nTests);

	for (size_t i = 0; i < nTests; ++i)
	{
		int nMotes = 0;
		Field field;
		ifs >> field.player >> nMotes;

		for (int j = 0; j < nMotes; ++j)
		{
			int mote;
			ifs >> mote;
			field.motes.push_back(mote);
		}
		std::sort(field.motes.begin(), field.motes.end());
		field.first = 0;
		field.last = field.motes.size() - 1;
		tests.push_back(field);
	}

	assert(tests.size() == nTests);
	return tests;
}

void consume (int &p, int &f, int&l, Motes &motes)
{
	for (int i = f; i <= l; ++i)
		if (p > motes[i])
		{
			p += motes[i];
			++f;
		}
		else break;
}

int changes(int p , int f, int l, Motes &motes)
{
	consume(p, f, l, motes);
	if (f > l)
		return 0;

	if (f == l)
		return 1;

	int a = std::numeric_limits<int>::max();
	if (p > 1)
	{
		a = changes(p + p -1, f, l, motes) + 1;
		if (a == 1)
			return 1;
	}

	int r = changes(p, f, l - 1, motes) + 1;

	return std::min(a, r);
}


int main(int argc, char *argv[])
{
	assert(argc > 1);

	std::string in = argv[1];

	out.open(in + ".out", std::ios_base::out | std::ios_base::trunc );

	Tests tests = readInput(in.c_str());

	for (int i = 0; i < tests.size(); ++i)
	{
		out << "Case #" << i + 1 << ": " << changes(tests[i].player, 0, tests[i].motes.size() - 1, tests[i].motes) << std::endl;
	}


	return 0;
}