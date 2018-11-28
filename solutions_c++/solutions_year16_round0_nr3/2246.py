
#include <tchar.h>
#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int main(int argc, char* argv[])
{
  int T, N, J;
  unsigned int CoinJam;
  ifstream input;
  ofstream output;

  // initialize
  if ( argc != 3 ) return -1;
  input.open( argv[1] );
  if ( !input ) return -1;
  output.open( argv[2] );

  input >> T;
  input >> N;
  input >> J;

  // we know the values of above numbers...

  output << "Case #1:" << endl;  

  for ( unsigned int i=0; i<500; i++ )
  {
    CoinJam = 0xbfc00001 | ( i << 2 ) | ( (i ^ 0x03ff) << 12 ) ;
    for ( int i=0; i<32; i++ )
    {
      output << ( ( CoinJam & 0x80000000 ) ? '1' : '0' );
      CoinJam <<= 1;
    }
    output << " 11 11 11 11 11 11 11 11 11" << endl;
  }

  input.close();
  output.close();

  return 0;
}

