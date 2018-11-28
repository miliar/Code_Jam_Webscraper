#include "library.hh"
Parser p;

void solve( TestCase t, uint32_t idx ){
	std::cout << "Case #" << idx+1 << ": ";
	
	int32_t needed = 0;
	int32_t sum_people = t.shyness[0];

	for( int32_t i = 1; i <= t.max_shyness; i++ ){
		if( i > sum_people ){
			needed += (i - sum_people);
			sum_people = i;
		}
		sum_people += t.shyness[i];
	}

	std::cout << needed << std::endl;
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