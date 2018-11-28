#include <cmath>
#include <iostream>
using namespace std;

int rev( int num )
{
  int tmp = 0;

  while ( num )
  {
    tmp *= 10;
    tmp += num % 10;
    num /= 10;
  }
  return tmp;
}

int main( )
{
  int caseCnt, A, B, nums, sq;

  cin >> caseCnt;
  for (int caseNr = 1; caseNr <= caseCnt; ++caseNr )
  {
    nums = 0;
    cin >> A >> B;
    for ( ; A <= B; ++A )
      if ( A == rev( A ) )
      {
        sq = (int) sqrt(A);
        if ( sq * sq == A && sq == rev( sq ) )
          ++nums;
      }
    cout << "Case #" << caseNr << ": " << nums << endl;
  }
  return 0;
}