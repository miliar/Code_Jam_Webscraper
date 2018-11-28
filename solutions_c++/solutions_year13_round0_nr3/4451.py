#include <iostream>
#include <math.h>
#include <vector>

using namespace std;

bool isPalindrome( int num )
{
  int reverse = 0;
  int temp = num;
  while( temp != 0 )
   {
      reverse = reverse * 10;
      reverse = reverse + temp%10;
      temp = temp/10;
   }
   return num == reverse;
}
 
int isPailinNSqaureAPalin( int num )
{
  double rootVal = sqrt( num );
  if( isPalindrome( num ) && ( rootVal * rootVal == (double)num ) && isPalindrome( rootVal ) )
    return 1;
  return 0;
}

int main()
{
  unsigned numOfTestCases( 0 );
  cin >> numOfTestCases;
  vector< int > finalResult;
  for( unsigned i = 0; i < numOfTestCases; ++i ) {
    int startVal( 0 );
    int endVal( 0 );
    cin >> startVal >> endVal;
    int kount( 0 );
    for( int j = startVal; j <= endVal; ++j )
      kount+= isPailinNSqaureAPalin( j );
    //cout<<"Case #"<<i+1<<": "<<kount<<endl;
    finalResult.push_back( kount );
  }
  for( unsigned k = 0; k < finalResult.size(); ++k )
    cout<<"Case #"<<k+1<<": "<<finalResult[k]<<endl;
  return 0;
}