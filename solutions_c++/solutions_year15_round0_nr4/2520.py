
#include <tchar.h>
#include <fstream>
#include <iostream>

using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
  int T, X, R, C;
  ifstream input;
  ofstream output;
  bool bRichard;

  if ( argc != 3 ) return -1;
  input.open( argv[1] );
  if ( !input ) return -1;
  output.open( argv[2] );

  input >> T;

  for ( int t=0; t < T; t++ )
  {
    input >> X;
	input >> R;
	input >> C;

	switch (X)
	{
	case 1:
	  bRichard = false; break;

	case 2:
	  bRichard = ( ( R*C ) % 2 ); break;

	case 3:
      bRichard = ( ( ( R*C ) % 3 ) || ( R*C < 6) ); break;

	case 4:
      bRichard = ( ( ( R*C ) % 4 ) || ( R*C < 12 ) ); break;

	default:
      bRichard = true;
	}
	output << "Case #" << t+1 << ": " << ( bRichard ? "RICHARD" : "GABRIEL" ) << endl;  
    
  }
  input.close();
  output.close();

  return 0;
}

