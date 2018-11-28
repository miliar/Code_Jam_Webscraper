#include <fstream>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <ttmath/ttmath.h>
using namespace std;

int main( int argc, char** argv )
{
  if( argc != 3 )
  {
    cout << "Mark, idiot, use parameters!" << endl;
    exit(1);
  }
  ifstream fin(argv[1]);
  ofstream fout(argv[2]);
  unsigned int T;
  fin >> T;

  for( unsigned int i = 0; i < T; i++ )
  {
    if( i != 0 )
    {
      fout << "\n";
    }
    fout << "Case #" << i+1 << ": ";

    ttmath::UInt<16> r, t, one = 1, two = 2, four = 4, eight = 8;
    fin >> r >> t;
    ttmath::UInt<16> answer = four*r*r - four*r + eight*t + one;
    answer.Sqrt();
    answer = answer + one - two*r;
    answer = answer / four;
    //double answer = ( one + two*r + ( four*r*r - four*r +
      //eight*t + one ).Sqrt() ) / 4.0;
    fout << answer;
  }

  fin.close();
  fout.close();
  return 0;
}