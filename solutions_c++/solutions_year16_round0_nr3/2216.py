#include<boost/multiprecision/cpp_int.hpp>
#include<iostream>
#include<algorithm>
#include<set>
#include<vector>
#include<ctime>
using boost::multiprecision::cpp_int;

int contains( std::vector< cpp_int > *ara, cpp_int number ) {
  int retval = 0;
  for( std::vector< cpp_int >::iterator i = ara -> begin( ); i != ara -> end( ); i++ ) {
    if( *i == number ) {
      return 1;
    }
  }
  return retval;
}

cpp_int dumbprimetest( cpp_int num, std::set< cpp_int > *divisors, std::vector< cpp_int > *bases ) {
  clock_t start = clock( );

  for( cpp_int k = 2; k < num/2+1; k++ ) {
    if( !(num%k) && divisors -> find( k ) == divisors -> end() && !contains( bases, k ) ) {
      return k;
    }

    if( (clock( ) - start)/(double)CLOCKS_PER_SEC > .01 ) {
      return 0;
    }

  }
  return 0;
}

cpp_int changebase( int64_t start, int l ) {
  if( l == 2 ) {
    cpp_int r(start);
    return r;
  }
  cpp_int r(0);
  cpp_int rl(l);
  for( int i = 0; i < 32; i++ ) {
    //r += !!(start & 1<<i) * pow( rl, i );
    r += ( ( start >> i ) & 1 ) * pow( rl, i );
  }
  return r;
}

void printstuff( int J, int64_t start, std::vector< cpp_int > *bases ) {
  std::cout<<changebase(start,10)<<' ';
  for( std::vector< cpp_int >::iterator i = bases -> begin( ); i != bases -> end( ); i++ ) {
    std::cout<<*i<<' ';
  }
  std::cout<<'\n';
}

int main(){
  int N, J;
  std::cin >> J;
  std::cin >> J;
  std::cin >> N;

  //std::cout<< J << ' ' << N << '\n';
  std::cout<<"Case #1:\n";

  int64_t start = 1 + ( (int64_t)1<<(J-1) );
  int count = 0;
  std::set< cpp_int > divisors;

  while( count != N ) {
    std::vector< cpp_int > bases;
    for( int l = 2; l <= 10; l++ ) {
      cpp_int temp = dumbprimetest( changebase( start, l ), &divisors, &bases );
      if( temp ) {
        bases.push_back( temp );
      } else {
        break;
      }
    }
    if( bases.size() == 9 ) {
      printstuff( J, start, &bases );
      count += 1;

      for( std::vector< cpp_int>::iterator i = bases.begin(); i != bases.end(); i++ ) {
        divisors.insert( *i );
      }
    }
    start += 2;
  }
}
