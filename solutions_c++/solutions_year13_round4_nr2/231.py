#include <stdio.h>
#include <vector>
#include <map>
#include <stdlib.h>
#include <string>
#include <set>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <fstream>

using namespace std;

ifstream in( "input.txt" );
ofstream out( "output.txt" );

void solveTest()
{
  long long N, P;
  in >> N >> P;
  P = (1LL << N) - P;
  long long cc1 = 0;
  long long cc2 = 0;
  long long ww = 0;
  long long res1 = -1;
  long long res2 = 0;
  long long cur2 = 0;
  for( long long i = N - 1; i >= 0; i-- ) {
    bool isWin = (P & (1LL << i)) != 0;
    if( isWin ) {
      if( res1 < 0 ) {
	res1 = 2 * ww;
      }
      cur2 = cur2 * 2 + 1;
    } else {
      res2 = std::max(res2, (1LL << N) - cur2 * 2 - 2); 
      ww = ww * 2 + 1;
    }
  }
  if( res1 < 0 ) { 
    res1 = (1LL << N) - 1;
  }
  if( res2 < 0 ) {
    res2 = 0;
  }
  if( res2 < (1LL << N) - cur2 - 1 ) {
    res2 = ( 1LL<<N) - cur2 - 1;
  }
  out << res1 << " " << res2 << "\n";
}

void run()
{
  int tn;
  in >> tn;
  for( int i = 1; i <= tn; i++ ) {
    out << "Case #" << i << ": ";
    solveTest();
  }
}

int main()
{
  run();
  return 0;
}
