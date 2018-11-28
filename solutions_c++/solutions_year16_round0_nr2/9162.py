#include <iostream>
#include <map>
#include <cmath>
#include <string>

using namespace std;

int GetNumOfTimes( string pancakes );

int main( )
{
  int numOfTestCases = 0;
  string pancakes = "";
  int result = 0;  
  
  cin >> numOfTestCases;
  for ( int i = 1 ; i <= numOfTestCases ; i++ )
  {
    cin >> pancakes;
    
    cout << "Case #" << i << ": ";
    cout << GetNumOfTimes( pancakes ) << endl;
  } // for
  
  return 0;
} // end main()

int GetNumOfTimes( string pancakes )
{
  int result = 0;  
  int position = 0;
  int maxPos = 0;
  int length = pancakes.length();
    
  for ( int i = 0 ; i < length ; i++ )
  {
    if ( pancakes[ i ] == '-' )
    {
      position += pow( 2, i );
      maxPos = i + 1;
    } // if
  } // for  
   
  while ( position > 1 )
  {
    // using floor() + 1, not ceil()    
    position = ( ( int ) pow( 2, floor( log2( position ) ) + 1 ) - 1 ) - position;
    result += 1; 
  } // while  
  
  result += position;  
  return result;
} // end GetNumOfTimes()






