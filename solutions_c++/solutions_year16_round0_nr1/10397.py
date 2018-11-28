#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <set>
#include <algorithm>
#include <iterator>

std::vector< std::uint32_t > readIntegerFile ( std::string filename ) {
  std::vector< std::uint32_t > values;

  std::ifstream is;
  is.open ( filename );
  std::istream_iterator< std::uint32_t > eos;
  std::istream_iterator< std::uint32_t > iit ( is );
  std::copy ( iit, eos, std::back_inserter ( values ) );
  is.close ( );

  return values;
}

void countSheep ( const int N, const int caseNumber, std::set< char > &checklist ) {
  std::fstream fs;
  fs.open ( "output.txt", std::fstream::out | std::fstream::app );

  if ( 0 == N ) {
    fs << "Case #" << caseNumber << ": INSOMNIA" << std::endl;
    return;
  }

  auto ntmp = N;
  auto i = 1;
  do {
    std::ostringstream os;
    os << ntmp;
    std::string sN = os.str ( );
    for(char c : sN) {
      checklist.insert(c);
    }
    if(10 == checklist.size()) {
      fs << "Case #" << caseNumber << ": " << sN << std::endl;
      break;
    }

    ++i;
    ntmp = i * N; 
  } while ( true );

  fs.close ( );
}

int main ( int argc, char *argv[] ) {
  if ( 2 == argc ) {
    std::string filename{argv[ 1 ]};

    auto values = readIntegerFile ( filename );
    if ( values[ 0 ] != values.size ( ) - 1 ) {
      std::cerr << "Invalid Data file" << std::endl;
      return EXIT_FAILURE;
    }

    std::set< char > checklist;
    for ( std::size_t i = 1; i < values.size ( ); ++i ) {
      countSheep ( values[ i ], i, checklist );
      checklist.clear();
    }
  }

  return EXIT_SUCCESS;
}
