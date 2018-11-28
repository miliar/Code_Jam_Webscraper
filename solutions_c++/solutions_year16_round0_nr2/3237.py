#include "library.hh"
Parser p;

bool happy( std::string in ){
	if( in.find_first_of('-') == std::string::npos )
		return true;
	else
		return false;
}

char inverse( char i ){
	if( i == '-' )
		return '+';
	if( i == '+' )
		return '-';
	return 0;
}

std::string flip( std::string in, int64_t num ){
	std::string tmp = in;

	for( int i = 0; i < num; i++ ){
		tmp[i] = inverse( tmp[i] );
	}
	return tmp;
}

void solve( TestCase t, uint32_t idx ){
	std::cout << "Case #" << idx+1 << ": ";

	std::string pancake = t.pancake;

	int iterations = 0;

	while( !happy(pancake) ){
		iterations++;

		size_t pos_m = pancake.find_last_of( '-' );
		size_t pos_p = pancake.find_last_of( '+' );

		// All negative
		if( pos_p == std::string::npos ){
			pancake = flip( pancake, pancake.size() );
			break;
		}

		if( pos_m > pos_p ){
			// Negatives at the end, flip everything ;(
			pancake = flip( pancake, pancake.size() );
		}

		if( pos_m < pos_p ){
			pancake = flip( pancake, pos_m+1 );
		}		
	}
	
	std::cout << iterations << std::endl;
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