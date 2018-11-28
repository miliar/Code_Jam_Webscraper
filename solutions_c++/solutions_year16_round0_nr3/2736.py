#include "library.hh"

using namespace std;

std::vector<int64_t> Parser::split_line_int( std::string & line ){
	std::vector<std::string> helper;
	std::vector<int64_t> result;
	boost::split( helper, line, boost::is_any_of(" ") );

	for( uint64_t i = 0; i < helper.size(); i++ )
		result.push_back( boost::lexical_cast<int64_t>( helper[i] ) );

	helper.clear();
	return result;
}

std::vector<std::string> Parser::split_line( std::string & line ){
	std::vector<std::string> result;
	boost::split( result, line, boost::is_any_of(" ") );
	return result;
}

// A typical sorting function for std::sort
bool Parser::sort_func( std::pair<int64_t, int64_t> a, std::pair<int64_t,int64_t> b ){
	return a.first < b.first;
	// return a.second < b.second:
}

void Parser::read_file( std::string filename ){
	cases.clear();

	std::fstream hnd_input( filename );
	std::string line;

	std::getline( hnd_input, line );
	T = boost::lexical_cast<uint64_t>( line );


	for( uint64_t i = 0; i < T; i++ ){
		TestCase t;
		std::string line;
		
		// Convert string to int
		// std::getline( hnd_input, line );
		// int a = boost::lexical_cast<int>( line );
		// t.N = a;

		// Split line into int's
		std::getline( hnd_input, line );
		std::vector<int64_t> res = split_line_int( line );
		t.N = res[0];
		t.J = res[1];

		// Split line into strings
		// std::vector<std::string> res = split_line( line );


		// std::sort( t.a.begin(), t.a.end() );
		// std::sort( t.a.begin(), t.a.end(), sort_func );

		cases.push_back( t );
	}	
}
