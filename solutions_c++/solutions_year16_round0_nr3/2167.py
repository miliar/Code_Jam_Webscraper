//============================================================================
// Name        : coin.cpp
// Author      : Antonello Gerbi
// Version     :
// Copyright   : 
// Description :
//============================================================================

#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include "infint/InfInt.h"

InfInt to10fromBase( const std::string & str, const unsigned int n )
{

  InfInt ret = 0;
  InfInt k = 1;

  for( unsigned int i = str.length(); i > 0; --i )
  {

    if( str.at( i - 1 ) == '1' ) ret += k;
    k *= n;
    
  }

  return ret;

}

std::string toBaseFrom10( InfInt n, const InfInt b )
{

  std::string ret;
  
  while( n != 0 )
  {
    
    ret = ( ( n % b == 0 ) ? "0" : "1" ) + ret;
    n /= b;
    
  }
  
  return ret;
      
}

InfInt isPrime( const InfInt n )
{

  for( unsigned int i = 2; i < 50; ++i )
    if( n % i == 0 ) return i;
  
  return 0;
    
}


int main( int argc, char *argv[] )
{

  std::string::size_type sz;

  std::ifstream inFile;
  std::ofstream outFile( "output" );
  inFile.open( argv[ 1 ] );
  
  outFile << "CASE #1:" << std::endl;
  
  std::string input;
  getline( inFile, input );
  unsigned int tests = std::stoi( input, &sz );
  
  for( unsigned int i = 0; i < tests; ++i )
  {

    getline( inFile, input );
    
    std::string buf;
    std::stringstream ss( input );

    unsigned int N, J;

    ss >> N;
    ss >> J;

    
    std::string nString( N - 2, '0' );
    nString = "1" + nString + "1";
    
    InfInt n, b;
    InfInt d[ J ][ 9 ];

    unsigned int j = 0;
    
    while( j < J )
    {

      bool isJamCoin = true;
      
      for( unsigned int k = 0; k < 9; ++k ) d[ j ][ k ] = 0;
      
      for( unsigned int k = 0; k < 9; ++k )
      {

        b = to10fromBase( nString, k + 2 );

        d[ j ][ k ] = isPrime( b );

        if( d[ j ][ k ] == 0 )
        {
          
          isJamCoin = false;
          k = 10;
          
        }
        
      }
      

      if( isJamCoin )
      {  

        outFile << nString << " ";
        
        for( unsigned int k = 0; k < 9; ++k ) outFile << d[ j ][ k ] << " ";
          
        outFile << std::endl;

        ++j;
        
      }

      n = to10fromBase( nString, 2 );
      n += 2;
      nString = toBaseFrom10( n, 2 );
      
    }
    
    
    
    
    
    
    
    
    
    
    
    

    
  }
  
  inFile.close();
  outFile.close();
	
	return 0;
	
}
