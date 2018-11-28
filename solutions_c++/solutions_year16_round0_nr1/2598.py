//============================================================================
// Name        : sheep.cpp
// Author      : Antonello Gerbi
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <array>
#include <string>
#include <fstream>

bool insomnia( unsigned int value )
{
  
  bool ret = false;
  
  if( value == 0 ) ret = true;
  
  return ret;

}

void countIfPresent( unsigned int value, std::array< bool, 10 > & presences )
{
  
  while( value > 0 )
  {
    
    unsigned int digit = value % 10;

    presences[ digit ] = true;
    
    value /= 10;
    
  }

}

bool allPresent( std::array< bool, 10 > & arr )
{

  bool ret = true;
  
  for( unsigned int i = 0; i < 10; ++i )
    if( !arr[ i ] ) ret = false;

  return ret;
  
}


int main( int argc, char *argv[] )
{

  std::string::size_type sz;

  std::ifstream file;
  std::ofstream outFile( "output" );
  file.open( argv[ 1 ] );
  
  std::string input;
  getline( file, input );
  unsigned int tests = std::stoi( input, &sz );

  
  unsigned int value, curValue;
  std::array< bool, 10 > presences;
  
  for( unsigned int i = 0; i < tests; ++i )
  {

    getline( file, input );
    
    value = std::stoi( input, &sz );
    
    if( insomnia( value ) ) outFile << "CASE #" << ( i + 1 ) << ": INSOMNIA" << std::endl;
    else
    {
      
      curValue = value;

      for( unsigned int i = 0; i < 10; ++i ) presences[ i ] = false;
      countIfPresent( value, presences );
      
      while( !allPresent( presences ) )
      {
        
        curValue += value;
        
        countIfPresent( curValue, presences );
        
      }
      
      outFile << "CASE #" << ( i + 1 ) << ": " << curValue << std::endl;
      
    }
    
  }
  
  file.close();
  outFile.close();
  
  /*
  std::ofstream outFile( "output" );
    
  for( unsigned int i = 0; i < 1000001; ++i ) outFile << i << "\n";
  outFile.close();*/
	
	return 0;
	
}
