
#include <tchar.h>
#include <fstream>
#include <iostream>
#include <string>

using namespace std;



int main( int argc, char* argv[] )
{
  int T;
  unsigned K, N;
  char aBuffer[1500];
  string str;

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
    input >> str;
    input >> K;
    strcpy( aBuffer, str.c_str() );
    N = str.length();
    for ( int i=0; i<N; i++ ) aBuffer[i] = ( aBuffer[i] - '+' ) /2  + '0';
    
    int j = 0;
    int nFlip = 0;

    while ( j+K < N )
    {
      if ( aBuffer[j] == '1' )
      {
        for ( int i=0; i<K; i++ ) { aBuffer[j+i] ^= 1; }
        nFlip++;
      }
      j++;
    }

    if ( aBuffer[j] == '1' )
    {
      nFlip++;
      for ( int i=0; i<K; i++ )
      {
        if ( aBuffer[j+i] == '0' )
        {
          nFlip = -1;
          break;
        }
      }
    }
    else
    {
      for ( int i=0; i<K; i++ )
      {
        if ( aBuffer[j+i] == '1' )
        {
          nFlip = -1;
          break;
        }
      }
    }

    output << "Case #" << t+1 << ": ";
    if ( nFlip >= 0 ) { output << nFlip; } else { output << "IMPOSSIBLE"; };    
    output << endl;  
  }

  input.close();
  output.close();

  return 0;
}

