#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <string>
#include <algorithm>

using namespace std;

vector<int> Evacuate( vector<int> & parties );
int GetTotal( vector<int> parties );

int main( )
{
  int numOfTestCases = 0;
  int numOfParties = 0;
  // string pancakes = "";
  // int result = 0;  
  
  cin >> numOfTestCases;
  for ( int i = 1 ; i <= numOfTestCases ; i++ )
  {    
    cin >> numOfParties;

    // cout << "hello: numOfParties: " << numOfParties << endl;

    // int parties[ numOfParties ] = { 0 };
    vector<int> parties; // ( numOfParties );
    for ( int party = 0 ; party < numOfParties ; party++ )
    {
      // cout << "party b: " << party << endl;

      // cin >> parties[ party ];
      // cout << "aaa: " << parties[ party ] << endl;
      int value = 0;
      cin >> value;
      // cout << "value: " << value << endl;

      parties.push_back( value );
      // cout << "party: " << party << endl;
      // cout << "aaa: " << parties[ party ] << endl;
    } // for

    // cout << "aaaaaaaa" << endl;
    cout << "Case #" << i << ": ";

    int size = 0;
    while ( ( size = Evacuate( parties ).size() ) && ( GetTotal( parties ) ) )
    {
      // cout << "here" << endl;
      ; // cout << result;
    } // while

    // cout << "aaabbbccc" << endl;
    
    cout << endl;
  } // for
  
  return 0;
} // end main()

vector<int> Evacuate( vector<int> &parties )
{
  // cout << "hello hello" << endl;

  int length = parties.size();
  int total = 0;

  // cout << "length: " << length << endl;
    
  for ( int i = 0 ; i < length ; i++ )
  {
    // cout << "parties: " << parties[ i ] << endl;

    total += parties[ i ];
  } // for  

  // cout << "total: " << total << endl;

  int maxer = 0;
  int maxer2 = 0;
  for ( int i = 0 ; i < length - 1 ; i++ )
  {
    if ( parties[ i + 1 ] >= parties[ maxer ] )
    {
      maxer2 = maxer;
      maxer = i + 1;
    }

  } // for

  if ( maxer == 0 )
  {
    maxer2 = 1;
    for ( int i = 1 ; i < length - 1 ; i++ )
    {
      if ( parties[ i + 1 ] >= parties[ i ] )
      {
        maxer2 = i + 1;
      }
    } // for
  } // if

  if ( parties[ maxer2 ] == parties[ maxer ] )
  {
    if ( ( parties[ maxer ] == 1 ) && ( total == 3 ) )
    {
      cout << ( char ) ( 'A' + maxer ) << " ";
      parties[ maxer ] = ( parties[ maxer ] - 1 );
    } // if
    else
    {
      cout << ( char ) ( 'A' + maxer ) << ( char ) ( 'A' + maxer2 ) << " ";
      parties[ maxer ] = parties[ maxer ] - 1;
      parties[ maxer2 ] = parties[ maxer2 ] - 1;
    } // else    
  } // if
  else
  {
    cout << ( char ) ( 'A' + maxer ) << " ";
    parties[ maxer ] = parties[ maxer ] - 1;
  } // else

  // if ( total - 1 > 1 )
  // {
  //   cout << ( char ) ( 'A' + maxer );
  //   cout << " ";
  //   parties[ maxer ] = parties[ maxer ] - 1;
  // } // if
  // else
  // {
  //   cout << ( char ) ( 'A' + i );
  //   parties[ i ] = parties[ i ] - 1;    
  // } // else 

  // for ( int i = 0 ; i < length ; i++ )
  // {
   
  //   if ( ( parties[ i ] ) > 0 )
  //   {
  //     if ( total - 1 > 1 )
  //     {
  //       cout << ( char ) ( 'A' + i );
  //       cout << " ";
  //       parties[ i ] = parties[ i ] - 1;
  //       break;
  //     } // if
  //     else 
  //     {
  //       cout << ( char ) ( 'A' + i );
  //       parties[ i ] = parties[ i ] - 1;
  //     } // else 
  //   } // if
  // } // for   

  return parties;
} // end Evacuate()



int GetTotal( vector<int> parties )
{
  int length = parties.size();
  int total = 0;

  for ( int i = 0 ; i < length ; i++ )
  {
    total += parties[ i ];
  } // for  

  return total;
}


