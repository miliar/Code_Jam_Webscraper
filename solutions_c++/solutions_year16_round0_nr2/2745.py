
#include <tchar.h>
#include <fstream>
#include <iostream>
#include <string>

using namespace std;


int main(int argc, char* argv[])
{
  int T;
  int n, k;
  char blank, happy;
  string stack;
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
	blank = '-';
	happy = '+';
	n = 0;
    input >> stack;
	k = stack.length()-1;
	while ( ( k>=0 ) && ( stack.at(k) == happy ) ) k--;

	while ( k>=0 )
	{
	  while ( ( k>=0 ) && ( stack.at(k) == blank ) ) k--;
	  std::swap( happy, blank );
	  n++;
	}

    output << "Case #" << t+1 << ": " << n << endl;  
  }
  input.close();
  output.close();

  return 0;
}

