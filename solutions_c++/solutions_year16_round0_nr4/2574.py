#include "library.hh"
Parser p;


uint64_t get_offset( uint64_t idx, uint64_t d, uint64_t K ){
	if( d <= 1 )
		return idx;

	return (static_cast<uint64_t>(idx)*static_cast<uint64_t>( std::pow( K, d-1 ) )) + get_offset( idx, d-1, K );
}

// Note: this will only work for small dataset!
void solve( TestCase t, uint32_t idx ){
	std::cout << "Case #" << idx+1 << ": ";

	if( t.S < t.K ){
		// Will not happen in small dataset; is wrong for large dataset.
		std::cout << "IMPOSSIBLE" << std::endl;
		return;
	}

	for( int64_t i = 0; i < t.K; i++ ){
		// uint64_t offset = get_offset( i, t.C, t.K ) + 1;
		std::cout << i+1 << " ";
	}
	std::cout << std::endl;
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