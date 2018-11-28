#include <algorithm>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <iterator>

// pi(r+2n-1)^2 - pi(r+2n-2)^2 = pi*[(4n-2)*r + 4n^2-4n+1 - (4n-4)*r - 4n^2+8n-4]
//                           = pi*[2r+4n-3]
// sum_n=1^N pi*[2r+4n-3] = pi[N(2r-3) + 2N(N+1)]
// pi[N(2r-3) + 2N(N+1)] = t*pi
// 2N^2 + N(2r-1) - t = 0

template <typename Container>
void readN(std::istream& is, Container& cont, size_t n)
{
	std::copy_n(std::istream_iterator<typename Container::value_type>(is), n,
		std::inserter(cont, cont.end()));
}

int main(int argc, const char* argv[])
{
	if (argc != 2)
	{
		std::cerr << "Usage: " << argv[0] << " <input-file>\n";
		return 1;
	}

	std::ifstream is(argv[1]);
	if (!is.good())
	{
		std::cerr << "Unable to open input file " << argv[1] << "\n";
		return 1;
	}

	int nr_cases;
	is >> nr_cases;
	if (!is.good())
	{
		std::cerr << "Failed to read number of test cases\n";
		return 1;
	}

	for (int icase = 1; icase <= nr_cases; ++icase)
	{
		unsigned long r, t;
		is >> r >> t;

		unsigned long N = 0;
		while (2*N*N + N*(2*r-1) <= t) ++N;

		std::cout << "Case #" << icase << ": " << N-1 << '\n';
	}

	return 0;
}
