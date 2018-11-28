#include "library.hh"
Parser p;

std::pair<bool,char> table[4][4] = {
	{std::make_pair( true, '1' ), std::make_pair( true, 'i' ), std::make_pair( true, 'j'), std::make_pair( true, 'k' )},
	{std::make_pair( true, 'i' ), std::make_pair( false, '1' ), std::make_pair( true, 'k'), std::make_pair( false, 'j' )},
	{std::make_pair( true, 'j' ), std::make_pair( false, 'k' ), std::make_pair( false, '1'), std::make_pair( true, 'i')},
	{std::make_pair( true, 'k' ), std::make_pair( true, 'j' ), std::make_pair( false, 'i'), std::make_pair( false, '1')}
};

uint32_t translate( char a ){
	uint32_t idx;
	switch( a ){
		case '1':
			idx = 0;
			break;
		case 'i':
			idx = 1;
			break;
		case 'j':
			idx = 2;
			break;
		case 'k':
			idx = 3;
			break;
		default:
			std::cerr << "ERROR" << std::endl;
			exit(1);
	};
	return idx;
}

std::pair<bool, char> multiply( std::pair<bool,char> a, std::pair<bool,char> b ){
	uint32_t idx_a, idx_b;

	idx_a = translate( a.second );
	idx_b = translate( b.second );

	std::pair<bool,char> x = table[idx_a][idx_b];
	bool sign = (a.first == b.first);

	x.first = (x.first == sign);
	return x;
}

bool check_ijk( std::pair<bool,char> product ){
	auto i = std::make_pair( true, 'i' );
	auto j = std::make_pair( true, 'j' );
	auto k = std::make_pair( true, 'k' );
	auto test = multiply( i, j );
	test = multiply( test, k );

	bool result;
	if( test.first == product.first && test.second == product.second ){
		result = true;
	}else{
		result = false;
	}
	return result;
}

bool check_jk( std::pair<bool,char> product ){
	auto j = std::make_pair( true, 'j' );
	auto k = std::make_pair( true, 'k' );
	auto test = multiply( j, k );

	bool result;
	if( test.first == product.first && test.second == product.second ){
		result = true;
	}else{
		result = false;
	}
	return result;
}

bool check_k( std::pair<bool,char> product ){
	auto test = std::make_pair( true, 'k' );

	bool result;
	if( test.first == product.first && test.second == product.second ){
		result = true;
	}else{
		result = false;
	}
	return result;
}


void solve( TestCase t, uint32_t idx ){
	std::cout << "Case #" << idx+1 << ": ";

	if( t.test.length()*t.L < 3 ){
		std::cout << "NO" << std::endl;
		return;
	}

	auto small_product = std::make_pair( true, t.test[0] );

	for( int32_t j = 1; j < t.L; j++ ){
		auto x = std::make_pair( true, t.test[j] );
		small_product = multiply( small_product, x );
	}

	auto product = small_product;
	for( int32_t j = 0; j < t.X-1; j++ ){
		product = multiply( product, small_product );
	}

	// Simple test: Does i*j*k == product?
	if( !check_ijk(product) ){
		std::cout << "NO" << std::endl;
		return;
	}

	// If yes: Detailed check
	std::vector< std::pair<bool,char> > full;

	for( int32_t i = 0; i < t.X; i++ ){
		for( int32_t j = 0; j < t.L; j++ )
			full.push_back( std::make_pair( true, t.test[j] ) );
	}

	std::vector<int32_t> split_i;
	auto cur = full[0];

	for( uint32_t i = 1; i < full.size(); i++ ){
		if( cur.first && cur.second == 'i' ){
			split_i.push_back( i );
		}

		cur = multiply( cur, full[i] );
	}

	std::vector<int32_t> split_j;

	for( auto d : split_i ){
		auto tmp = full.begin() + d;

		auto jk_prod = *tmp;
		for( uint32_t i = d+1; i < full.size(); i++ ){
			jk_prod = multiply( jk_prod, full[i] );
		}

		if( !check_jk( jk_prod ) )
			continue;

		auto cur_j = *tmp;
		for( uint32_t i = d+1; i < full.size(); i++ ){
			if( cur_j.first && cur_j.second == 'j' ){
				split_j.push_back( i );
			}

			cur_j = multiply( cur_j, full[i] );
		}
	}


	for( auto d : split_j ){
		auto tmp = full.begin() + d;

		auto k_prod = *tmp;
		for( uint32_t i = d+1; i < full.size(); i++ ){
			k_prod = multiply( k_prod, full[i] );
		}

		if( check_k( k_prod ) ){
			std::cout << "YES" << std::endl;
			return;
		}
	}
	std::cout << "NO" << std::endl;
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