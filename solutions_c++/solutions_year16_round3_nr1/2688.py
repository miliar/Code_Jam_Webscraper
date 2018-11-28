#include "library.hh"

#include <string>
#include <vector>
#include <algorithm>

Parser p;

char int_to_letter( int i ){
  return (char)(i+65);
}

bool test( std::vector<int64_t> & party ){
  auto m = std::max_element( party.begin(), party.end() );
  int idx_m = std::distance( party.begin(), m );

  int sum = 0;
  for( int i = 0; i < party.size(); i++ ){
    if( i== idx_m )
      continue;
    sum += party[i];
  }

  if( *m > sum )
    return false;
  else
    return true;
}

bool flush( std::vector<int64_t> & p ){
  int val = 0;

  for( auto v : p ){
    if( val == 0 )
      val = v;

    if( v != val )
      return false;
  }
  return true;
}

bool above( std::vector<int64_t> & p, int t ){
  for( auto d : p ){
    if( d > t )
      return true;
  }
  return false;
}

void remove_two_max( std::vector<int64_t> & party ){
  auto m1 = std::max_element( party.begin(), party.end() );
  (*m1)--;
  std::cout << int_to_letter( std::distance( party.begin(), m1 ) );
  auto m2 = std::max_element( party.begin(), party.end() );

  if( *m2 <= 0 )
    return;

  (*m2)--;
  std::cout << int_to_letter( std::distance( party.begin(), m2 ) ) << " ";
}

void remove_one_max( std::vector<int64_t> & party ){
  auto m1 = std::max_element( party.begin(), party.end() );
  (*m1)--;
  std::cout << int_to_letter( std::distance( party.begin(), m1 ) ) << " ";
}

void solve( TestCase t, uint32_t idx ){
	std::cout << "Case #" << idx+1 << ": ";

  auto party = t.parties;

  if( party.size() == 2 ){
    while( above( party, 0 ) ){
      remove_two_max( party );
    }

    std::cout << std::endl;
    return;
  }

  while( above( party, 2 ) ){
    remove_one_max( party );
  }

  while( above( party, 1 ) ){
    remove_two_max( party );
  }

  int count = 0;
  for( auto d : party )
    if( d == 1 )
      count++;

  if( count%2 == 1 )
    remove_one_max( party );
  
  while( above( party, 0 ) ){
    remove_two_max( party );

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