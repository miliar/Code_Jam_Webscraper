#include <tchar.h>
#include <fstream>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;



const char * aLetters[10] = { "ZERO", "TWO", "SIX", "SEVEN", "FIVE", "FOUR", "ONE", "EIGHT", "NINE", "THREE" };
const char         aX[10] = { 'Z', 'W', 'X', 'S', 'V', 'F', 'O', 'G', 'I', 'R' };
const char     aDigit[10] = { '0', '2', '6', '7', '5', '4', '1', '8', '9', '3' };

int aLetterCount[26];
int aDigitCount[26];

int main( int argc, char* argv[] )
{
  int T;
  int n;
  char c;

  ifstream input;
  ofstream output;

  std::string sIn, sOut;

  // initialize
  if ( argc != 3 ) return -1;
  input.open( argv[1] );
  if ( !input ) return -1;
  output.open( argv[2] );
  input >> T;

  for ( int t=0; t < T; t++ )
  {
    sOut.clear();
    for ( int i=0; i<26; i++ )
    {
      aLetterCount[i] = 0;
      aDigitCount[i] = 0;
    }
    input >> sIn;

    for ( int i=0; i<sIn.size(); i++ )
    {
      c = sIn.at(i)-'A';
      aLetterCount[c]++;
    }

    for ( int i=0; i<10; i++ )
    {
      c = aX[i]-'A';
      n = aLetterCount[c];
      for ( int j=0; j<n; j++ ) sOut.push_back(aDigit[i]);
      for ( int j=0; j<strlen( aLetters[i] ); j++ )
      {
        aLetterCount[aLetters[i][j]-'A'] -= n;
      }
    }
    sort(sOut.begin(), sOut.end());

    output << "Case #" << t+1 << ": " << sOut << endl;  
  }
  input.close();
  output.close();

  return 0;
}

