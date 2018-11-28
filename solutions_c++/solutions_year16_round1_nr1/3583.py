#ifndef __LIBRARY_HH__
#define __LIBRARY_HH__

// Typical includes
#include <string>
#include <vector>
#include <boost/lexical_cast.hpp>
#include <boost/algorithm/string.hpp>
#include <fstream>
#include <cstdint>
#include <iomanip>

#include <utility>

// EDIT HERE...
struct TestCase{
	std::string input;
};


class Parser{
	public:
		void read_file( std::string filename );
		std::vector<int64_t> split_line_int( std::string & line );
		std::vector<std::string> split_line( std::string & line );

		bool sort_func( std::pair<int64_t, int64_t> a, std::pair<int64_t,int64_t> b );

		// I realize this is bad style, but in the interest of time I make them public
		std::vector<TestCase> cases;
		uint64_t T;
};

#endif