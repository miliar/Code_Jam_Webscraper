#include "library.hh"

std::vector<int32_t> Parser::split_line_int( std::string & line ){
	std::vector<std::string> helper;
	std::vector<int32_t> result;
	boost::split( helper, line, boost::is_any_of(" ") );

	for( uint32_t i = 0; i < helper.size(); i++ )
		result.push_back( boost::lexical_cast<int32_t>( helper[i] ) );

	helper.clear();
	return result;
}

std::vector<std::string> Parser::split_line( std::string & line ){
	std::vector<std::string> result;
	boost::split( result, line, boost::is_any_of(" ") );
	return result;
}

// A typical sorting function for std::sort
bool Parser::sort_func( std::pair<int32_t, int32_t> a, std::pair<int32_t,int32_t> b ){
	return a.first < b.first;
	// return a.second < b.second:
}

void Parser::read_file( std::string filename ){
	cases.clear();

	std::fstream hnd_input( filename );
	std::string line;

	std::getline( hnd_input, line );
	T = boost::lexical_cast<uint32_t>( line );

	for( uint32_t i = 0; i < T; i++ ){
		TestCase t;
		std::string line;
		
		// Convert string to int
		//std::getline( hnd_input, line );
		//int32_t a = boost::lexical_cast<int32_t>( line );
		//t.N 	  = a;

		//std::getline( hnd_input, line );
		//string a = boost::lexical_cast<string>( line );
		//t.pencake = line;

		// Split line into int's
	    std::getline( hnd_input, line );
		
		std::vector<int32_t> res = split_line_int( line );
		t.K = res[0];
		t.C = res[1];
		t.S = res[2];

		// Split line into strings
		// std::vector<std::string> res = split_line( line );


		// std::sort( t.a.begin(), t.a.end() );
		// std::sort( t.a.begin(), t.a.end(), sort_func );

		cases.push_back( t );
	}	
}
