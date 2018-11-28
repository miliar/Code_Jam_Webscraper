#include <iostream>
#include <map>
#include <cmath>

using namespace std;

int GetResult( int chosenNum );

int main( )
{
  long long numOfTestCases = 0;
  int result = 0;
  int chosenNum = 0;  
  
  cin >> numOfTestCases;
  for ( int i = 1 ; i <= numOfTestCases ; i++ )
  {
    cin >> chosenNum;
    
    cout << "Case #" << i << ": ";
    if ( result = GetResult( chosenNum ) )
    {
      cout << result << endl;
    }
    else
    {
      cout << "INSOMNIA"  << endl;
    } // else    
  } // for
  
  return 0;
} // end main()


int GetResult( int chosenNum )
{
  int currentVal = chosenNum;
  map< int, bool > mymap;
  
  int multiplier = 1;
  while ( currentVal )
  {
    int tempVal = currentVal;
    for ( int tempVal = currentVal ; tempVal != 0 ; tempVal /= 10 )
    { 
      mymap[ tempVal % 10 ] = true;
    } // for  
    
    if (  mymap.size() == 10 )
    {
      return currentVal;
    } // if
    
    currentVal = chosenNum * ++multiplier;
  } // while
  
  return 0;
} // end GetResult()






