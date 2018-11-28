/**
 * @file cookieClicker.cpp
 * @brief Template that opens a file and reads the stream
 */
#include <iomanip>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <math.h>

double getTime( double _C, double _F, double _X );

/**
 * @function main
 */
int main( int argc, char* argv[] ) {

  if( argc != 2 ) {
    std::cout << "Syntax: "<<argv[0]<<" "<<argv[1]<<std::endl;
    return -1;
  }

  std::ifstream input;
  std::ofstream output;
  std::string line;
  int T; // Number of test cases
  double C, F, X; // Factory cost, increase in rate, cookies required

  input.open( argv[1], std::ios::in );
  output.open( "cookiesResult.txt", std::ios::out );

  if( input.is_open() ) {
    std::getline( input, line );
    std::stringstream( line ) >> T;
    
    for( int i = 0; i < T; i++ ) {
      std::cout << "Test case: "<< i+1<< std::endl;
      std::getline( input, line );
      std::cin.precision(8);
      std::stringstream( line ) >> C >> F >> X;

      std::cout << " C: "<< C << " F: "<< F<< " X: "<<std::fixed<< X << std::endl;

      double cookieTime = getTime( C, F, X );

      std::cout.precision(10);
      output << "Case #"<<i+1<<": "<<std::fixed<<cookieTime<<std::endl;
    }
    
  } else {
    std::cout << "[X] Error opening input file"<< std::endl;
  }
  
  output.close();
  input.close();

  return 0;
}

/**
 * @function getTime
 */
double getTime( double _C, double _F, double _X ) {

  int i = 0;
  double cookieTime = 0;

  do {

    if( (_X - _C) / (2.0 + i*_F ) < _X / ( 2 + (i+1)*_F ) ) {
      cookieTime = cookieTime + (_X /(2.0 + i*_F));
      break;
    } else {
      cookieTime = cookieTime + (_C/(2.0+i*_F)) ;
    }
    
    i++;
  } while( i < 10000 );
  
  return cookieTime;
}
