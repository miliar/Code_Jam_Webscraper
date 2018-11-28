//
// competition.cpp
//
// Copyright (c) 2016, Mike Waney
//
// Main runner for GoogleCodeJam competition projects
//

//#include <algorithm>
//#include <cassert>
//#include <chrono>
//#include <cctype>
//#include <fstream>
//#include <functional>
#include <iostream>
//#include <istream>
//#include <map>
//#include <sstream>
#include <string>

//#include <array>
#include <vector>
//#include <deque>
//#include <list>
//#include <forward_list>
//#include <set>				// std::set and std::multiset
//#include <map>				// std::map and std::multimap
//#include <unordered_set>		// std::unordered_set and std::unordered_multiset
//#include <unordered_map>		// std::unordered_map and std::unordered_multimap
//#include <stack>				// std::stack container adaptor
//#include <queue>				//  std::queue and std::priority_queue container adaptors

void codejam_countingsheep(std::istream& sin, std::ostream& sout)
{
	int num_tests;
	sin >> num_tests;

	std::vector<int> vi;
	vi.reserve(10);

	for (int ntest = 1; ntest <= num_tests; ntest++)
	{
		sout << "Case #" << ntest << ":"; // can prepad spaces

		long long num;
		sin >> num;

		vi.assign(10, 0);
		int num_found = 0;
		//int max_tries = 200;
		int max_tries = 1000000;
		long long multiple = 0;

		//auto t0 = std::chrono::high_resolution_clock::now();

		while (num_found < 10 && max_tries)
		{
			multiple += num;
			std::ldiv_t dv{}; dv.quot = multiple;
			while (dv.quot > 0)
			{
				dv = std::ldiv(dv.quot, 10);
				if (vi[dv.rem] == 0)
				{
					vi[dv.rem] = 1;
					num_found++;
				}
			}
			max_tries--;
		}

		if (max_tries == 0)
			sout << " INSOMNIA";
		else
			sout << " " << multiple;

		if (ntest < num_tests) sout << "\n";

		//auto t1 = std::chrono::high_resolution_clock::now();
		//std::cerr << std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count() << " microseconds passed" << "\n";
	}
}

int main(int argc, char** argv)
{
	std::ios_base::sync_with_stdio(false);

	// mange input stream
	//std::ifstream fsin("A-small-attempt0.in");
	//assert(fsin.is_open());

	// mange output stream
	//std::ofstream fsout("A-small-attempt0.out", std::ios::out | std::ios::trunc);
	//assert(fsout.is_open());

	codejam_countingsheep(std::cin, std::cout);

	//fsin.close();
	std::cout.flush();
	//fsout.close();

	// pause the command line
	//std::cerr << "any key\n";
	//std::cin.get();

	return 0;
}