//============================================================================
// Name        : pancakes.cpp
// Author      : Antonello Gerbi
// Version     :
// Copyright   : 
// Description :
//============================================================================

#include <iostream>
#include <vector>
#include <string>
#include <fstream>

std::vector< bool > stringToArray( const std::string str )
{

  std::vector< bool > ret;;
  ret.resize( str.length() );

  for( unsigned int i = 0; i < str.length(); ++i )
    ( str.at( i ) == '+' ) ? ret[ i ] = true : ret[ i ] = false;

  return ret;
  
}

void print( const std::vector< bool > & pancakes )
{

  for( unsigned int i = 0; i < pancakes.size(); ++i ) 
    ( pancakes[ i ] ) ? std::cout << "+" : std::cout << "-";
   
  std::cout << std::endl;
  
  return;

}

std::vector< bool > trim( const std::vector< bool > & pancakes )
{

  std::vector< bool > ret = pancakes;
  
  unsigned int n = pancakes.size();
  bool sideUp = true;
  
  while( sideUp && n > 0 )
  {
    
    if( !pancakes[ n - 1 ] )
      sideUp = false;
    else
      n -= 1;
    
  }
  
  ret.resize( n );
  
  return ret;
  
}


std::vector< bool > flip( const std::vector< bool > & pancakes, const unsigned int n )
{

  std::vector< bool > ret = pancakes;
  
  for( unsigned int i = 0; i < n; ++i )
    ( pancakes[ n - i - 1 ] ) ? ret[ i ] = false : ret[ i ] = true;
  
  return ret;
  
}


unsigned int turnAll( const std::vector< bool > & pancakes, unsigned int n )
{

  std::vector< bool > trimmed = trim( pancakes );
  unsigned int ret;
  
  if( trimmed.size() == 0 ) return n;
  else if( !trimmed[ 0 ] ) ret = turnAll( flip( trimmed, trimmed.size() ), n + 1 );
  else
  {
    
    bool sideUp = true;
    unsigned int k = 1;
    
    while( sideUp )
    {
      
      if( !trimmed[ k ] ) sideUp = false;
      else ++k;
      
    }
    
    ret = turnAll( flip( trimmed, k ), n + 1 ); 
    
  }

  return ret;
  
}


int main( int argc, char *argv[] )
{

  std::string::size_type sz;

  std::ifstream inFile;
  std::ofstream outFile( "output" );
  inFile.open( argv[ 1 ] );
  
  std::string input;
  getline( inFile, input );
  unsigned int tests = std::stoi( input, &sz );
  
  std::vector< bool > pancakes;
  
  for( unsigned int i = 0; i < tests; ++i )
  {

    getline( inFile, input );
    
    pancakes = stringToArray( input );

    outFile << "CASE #" << ( i + 1 ) << ": " << turnAll( pancakes, 0 ) << std::endl;
    
  }
  
  inFile.close();
  outFile.close();
	
	return 0;
	
}
