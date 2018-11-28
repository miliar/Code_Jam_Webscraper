#include <iostream>
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
    int answer = 0;
    string result = "";
    int currentCardNumber = 0;
    int selectedRow = 0;
    int possibleSelection[ 4 ] = { 0 }; // int possibleSelection[ 2 ][ 4 ] = { 0 };
    
    for ( int round = 0 ; round < 2 ; round++ )
    {
      cin >> selectedRow;
      for ( int row = 1 ; row <= 4 ; row++ )
      {
        for ( int column = 0 ; column < 4 ; column++ )
        {
          cin >> currentCardNumber;
          if ( selectedRow == row )
          {
            // possibleSelection[ round ][ column ] = currentCardNumber;
            if ( round == 0 )
            {
              possibleSelection[ column ] = currentCardNumber;
            } // if 
            else if ( round == 1 )
            {
              for ( int s = 0 ; s < 4 ; s++ )
              {
                if ( currentCardNumber == possibleSelection[ s ] )
                {
                  answer = ( answer == 0 ? currentCardNumber : -1 );
                } // if
              } // for
            } // else if
          } // if          
        } // for
      } // for 
    } // for 
    
    if ( answer == 0 )
    {
      result = "Volunteer cheated!";
    } // if
    else if ( answer == -1 )
    {
      result = "Bad magician!"; 
    } // else if
    else
    {
      // result = to_string( answer );
      // result = std::to_string( answer );
      stringstream sstream;
      sstream << answer;
      result = sstream.str();
    } // else
    
    cout << "Case #" << caseOrder << ": " << result << endl;
  } // for
  
  
} // end main()
