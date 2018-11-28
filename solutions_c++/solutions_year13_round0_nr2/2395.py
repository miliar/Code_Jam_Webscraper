#include <iostream>
#include <string>
#include <cassert>
#include <vector>
#include <fstream>
#include <cstdint>
#include <cmath>
#include <algorithm>


std::ofstream out;

typedef std::vector<size_t> Line;
typedef std::vector<Line> Lawn;

typedef std::vector<Lawn> Lawns;


Lawns readInput(const char* fn)
{
	std::ifstream ifs(fn);
	assert(ifs.is_open());

	size_t nLawns = 0;
	ifs >> nLawns;

	Lawns lawns(nLawns);

	for (int n = 0; n < nLawns; ++n)
	{
		size_t h, w;
		ifs >> h >> w;

		Lawn &lawn = lawns[n];

		for (int i = 0; i < h; ++i)
		{
			Line line;
			for (int j = 0; j < w; ++j)
			{
				size_t c;
				ifs >> c;
				line.push_back(c);
			}
			lawn.push_back(line);
		}
	}
	return lawns;
}

bool validCell(const Lawn &lawn, size_t i, size_t j)
{
	size_t h = lawn.size();
	size_t w = lawn[0].size();

	size_t c = lawn[i][j];

	bool vert = true;
	for (int k = 0; k < h; ++k)
		if ( k != i && lawn[k][j] > c)
		{
			vert = false;
			break;
		};

	bool hor = true;
	for (int k = 0; k < w; ++k)
		if ( k != j && lawn[i][k] > c)
		{
			hor = false;
			break;
		}

	return vert || hor;
}

bool valid(const Lawn &lawn)
{

	size_t h = lawn.size();
	size_t w = lawn[0].size();
	for (int i = 0; i < h; ++i)
		for (int j = 0; j < w; ++j)
		{
			if (!validCell(lawn, i, j))
				return false;
		}

	return true;
}

	
int main(int argc, char *argv[])
{
	assert(argc > 1);

	std::string in = argv[1];

	out.open(in + ".out", std::ios_base::out | std::ios_base::trunc );

	Lawns lawns = readInput(in.c_str());

	size_t size = lawns.size();

	for (int i = 0; i < size; ++i)
	{
		
		out << "Case #" << i + 1 << ": " << (valid(lawns[i]) ? "YES" : "NO") << std::endl;
	}

	return 0;
}