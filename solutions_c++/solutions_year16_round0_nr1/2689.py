
#include <tchar.h>
#include <fstream>
#include <iostream>
#include <string>

using namespace std;


void CheckDigits( unsigned int x, unsigned int & m )
{
  while ( x )
  {
    m |= 1 << ( x % 10 );
    x /= 10;
  }
}


int main( int argc, char* argv[] )
{
  int T;
  unsigned int N, A, mdig;

  ifstream input;
  ofstream output;

  // initialize
  if ( argc != 3 ) return -1;
  input.open( argv[1] );
  if ( !input ) return -1;
  output.open( argv[2] );
  input >> T;

  for ( int t=0; t < T; t++ )
  {
    input >> N;

    if ( N == 0 )
    {
      output << "Case #" << t+1 << ": INSOMNIA" << endl;  
    }
    else
    {
      mdig = 0;
      A = N;
     do
      {
        CheckDigits( A, mdig );
        A += N;
      }
      while ( mdig < 0x3ff );
      output << "Case #" << t+1 << ": " << (A-N) << endl;  
    }
  }
  input.close();
  output.close();

  return 0;
}

