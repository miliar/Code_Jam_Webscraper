#include "library.hh"
Parser p;

void solve( TestCase t, uint32_t idx ){
	std::cout << "Case #" << idx+1 << ": ";
	

	int32_t Y = 0;
	int32_t Z = 0;
	std::vector<int32_t> diffs;
	for( uint32_t i = 0; i < t.M.size()-1; i++ ){
		int32_t diff = t.M[i] - t.M[i+1];
		diffs.push_back( diff );
		if( diff >= 0 )
			Y += diff;
	}

	int32_t max = 0;
	for( auto d : diffs )
		if( d > max )
			max = d;
	// This is the rate! Now multiply by time
	Z = max * (t.N-1);

	// Now it might have been that the plate was empty in between, so substract
	for( uint32_t i = 0; i < t.M.size()-1; i++ )
		if( t.M[i] < max )
			Z -= (max-t.M[i]);


	std::cout << Y << " " << Z << std::endl;
}

int32_t main( int32_t argc, char ** argv ){

	std::string argument( argv[1] );
	std::vector<TestCase> cases;

	p.read_file( argument );
	cases = p.cases;

	for( uint32_t i = 0; i < p.cases.size(); i++ ){
		solve( p.cases[i], i );
	}

	return 0;
}