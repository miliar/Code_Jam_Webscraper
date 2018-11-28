#include <iostream>
#include <string>
#include <cassert>
#include <vector>
#include <fstream>
#include <cstdint>
#include <cmath>
#include <algorithm>

typedef std::pair<uint64_t, uint64_t> Lim;
typedef std::vector<Lim> Lims;

std:: ofstream out;

typedef std::vector<uint64_t> Pals;

Lims readInput(const char* fn)
{
	std::ifstream ifs(fn);


	assert(ifs.is_open());

	size_t nLims = 0;
	ifs >> nLims;

	Lims lims(nLims);


	for (size_t n = 0; n < nLims; ++n)
	{
		ifs >> lims[n].first >> lims[n].second;
	}

	return lims;
}

uint64_t pal(uint64_t n)
{
	char s[22];
	itoa(n, s, 10);
	size_t len = strlen(s);

	for (size_t i = 0, j = len - 1; i < j; ++i, --j)
	{
		if (s[i] != s[j])
			return 0;			
	}

	return n;
}

Pals gen(uint64_t s, uint64_t e)
{
	uint64_t ss = sqrt( double(s) );
	uint64_t ee = sqrt( double(e) );

	Pals pals;

	uint64_t n = 0;
	for (uint64_t i = ss; i <= ee; ++i)
		if ( (pal(i) > 0) && ( n = pal(i*i)) && (n >= s) && (n <= e)  )
			pals.push_back(n);

	return pals;
}


int main(int argc, char *argv[])
{
	assert(argc > 1);

	std::string in = argv[1];

	out.open(in + ".out", std::ios_base::out | std::ios_base::trunc );

	Lims lims = readInput(in.c_str());

	Pals pals  = gen (1, 100000000000000);

	size_t size = lims.size();

	for (int i = 0; i < size; ++i)
	{
		const Lim &lim = lims[i];
		out << "Case #" << i + 1 << ": " <<
			std::count_if(pals.begin(), pals.end(), [&lim](uint64_t n){
			return ( (n >= lim.first) && (n <=lim.second)) ;}) << std::endl;
	}


	return 0;
}

