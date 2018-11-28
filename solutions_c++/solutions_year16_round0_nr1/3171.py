#include "library.hh"
Parser p;

bool all_digits( std::vector<bool> & vec ){
	bool res = true;
	for( auto b : vec ){
		res = res && b;
	}
	return res;
}

void set_digits( std::vector<bool> & vec, int64_t number ){
	while( number > 0 ){
		int digit = number%10;
		vec[digit] = true;
		number = number/10;
	}
}

void solve( TestCase t, uint32_t idx ){
	std::cout << "Case #" << idx+1 << ": ";

	std::vector<bool> digits( 10, false );

	
	int64_t base = t.N;
	int64_t factor = 1;

	int64_t number = factor * base;

	if( number <= 0 ){
		std::cout << "INSOMNIA" << std::endl;
		return;
	}

	set_digits( digits, number );

	while( !all_digits( digits ) ){
		factor++;
		number = factor * base;
		
		set_digits( digits, number );
	}

	std::cout << number << std::endl;

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