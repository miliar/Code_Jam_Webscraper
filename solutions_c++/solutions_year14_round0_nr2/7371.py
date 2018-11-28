#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <string>
#include <sstream>

using namespace std;

int main()
{
  int testCases = 0;
  cin >> testCases;
  
  for ( int caseOrder = 1 ; caseOrder <= testCases ; caseOrder++ )
  {
    double answer = 0;
    int nth = 0;
    double rate = 0;
    
    double cost = 0;
    double fRate = 0;
    double target = 0;
    
    cin >> cost >> fRate >> target;
    
    while ( ( ( 2 * cost ) + ( ( nth + 1 ) * cost * fRate ) ) < ( target * fRate ) )
    {
      nth += 1;
    } // while
    
    answer = target / ( 2 + ( nth * fRate ) );
    
    for ( int i = ( nth - 1 ) ; i >= 0 ; i-- )
    {
      answer += ( cost / ( 2 + ( i * fRate ) ) );
    } // for 
    
    cout << "Case #" << caseOrder << ": " << fixed << setprecision( 7 ) << answer << endl;
  } // for
  
  return 0;
} // end main()
