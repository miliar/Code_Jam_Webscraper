
#include <tchar.h>
#include <fstream>
#include <iostream>

using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
  int T, N, S, F;
  int standing;
  char c;
  ifstream input;
  ofstream output;

  if ( argc != 3 ) return -1;
  input.open( argv[1] );
  if ( !input ) return -1;
  output.open( argv[2] );

  input >> T;

  for ( int t=0; t < T; t++ )
  {
    input >> N;
	F = 0;
	standing = 0;
    for ( int i=0; i < N+1; i++ )
    {
      input >> c;
	  S = c-'0';
	  if ( standing+F < i ) F = i-standing; 
	  standing += S;
    }
	output << "Case #" << t+1 << ": " << F << endl;  
    
  }
  input.close();
  output.close();

  return 0;
}

