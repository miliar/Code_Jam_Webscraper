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
#include <cmath>
#include <utility>
#include <algorithm>

using namespace std;
// EDIT HERE...
struct TestCase{
	//int64_t D;
	//int64_t K;
	//int64_t N;
	string alphabet;
	
};


class Parser{
	public:
	void read_file( std::string filename );
		//template<typename T>
		std::vector<int> split_line_int( std::string & line );
		std::vector<std::string> split_line( std::string & line );
		bool sort_func( std::pair<int32_t, int32_t> a, std::pair<int32_t,int32_t> b );
		// I realize this is bad style, but in the interest of time I make them public
		std::vector<TestCase> cases;
		uint32_t T;
};

#endif
