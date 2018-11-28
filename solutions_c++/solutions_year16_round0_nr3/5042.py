#include <iostream>
#include <map>
#include <cmath>
#include <string>

using namespace std;

int GetNumOfTimes( string pancakes );

int main( )
{
  long long numOfTestCases = 0;
  string pancakes = "";
  long long N = 0; // length
  long long J = 0; // distinct numbers
  long long result = 0;  
  
  cin >> numOfTestCases;
  for ( long long test = 1 ; test <= numOfTestCases ; test++ )
  {
    cin >> N;
    cin >> J;
    
    cout << "Case #" << test << ":" << endl;
    
    // return 0;
    
    long long pos = N - 1;
    
    // run distinct times
    long long distinct = 0;
    // while ( distinct < J )
    // {       
      long long ins = pow( 10, N - 2 );
      
      // cout << "ins: " << ins << endl;
      
      for ( long long addi = 0 ; addi < ins ; addi++  )
      {
        
        // cout << "addi: " << addi << endl;
        
        long long value = pow( 10, ( N - 1 ) ) + 1;
        long long all[ 11 ] = { 0 };
        
        for ( long long i = 2 ; i <= 10; i++ )
        {
          all[ i ] = pow( i, ( N - 1 ) ) + 1;
        } // for
        
        int n = 1;
        long long tempAddi = addi;
        while ( tempAddi > 0 )
        {
          // value += ( addi % 2 ) * pow( 10, n );        
          // cout << "tempAddi: " << tempAddi << " n: " << n << endl;
          
          for ( int i = 2 ; i <= 10; i++ )
          {
            if ( tempAddi % 2 )
            {
              all[ i ] += pow( i, n );  
            }            
          } // for
          
          n++;
          tempAddi /= 2;  
        } // while
        
        // cout << "all[ 10 ]: " << all[ 10 ] << endl;
        
        long long number = 0;      
        long long divisors[ 10 ] = { 0 };
        bool isThis = true;
        for ( long long i = 2 ; i <= 10; i++ )
        {
          // number = pow( i, pos ) + 1;
          long long from = 2;
          long long curr = from;
          long long number = all[ i ];
          long long to = floor( sqrt( all[ i ] ) );
          while ( curr <= to )
          {
            if ( all[ i ] % curr == 0 )
            {
              divisors[ i ] = all[ i ] / curr;
            }
            
            curr++;
          }
          
          // cout << "divisors[ 3 ]: " << divisors[ 3 ] << endl;
          
          if ( ! divisors[ i ] )
          {
            isThis = false;
            break;
          } // if
          
        } // for
        
        
        if ( isThis )
        {
          distinct++;
        
          // cout << "distinct: " << distinct << endl;
          cout << all[ 10 ];
          
          for ( int r = 2 ; r <= 10; r++ )
          {
            cout << " " << divisors[ r ];
          }
          
          cout << endl;
          
          
          
          if ( distinct == J )
          {
            break;
          } // if  
        } // if
            
      } // for
      
    // } // while
  } // for
  
  return 0;
} // end main()

int GetNumOfTimes( string pancakes )
{
  long long result = 0;  
  long long position = 0;
  long long maxPos = 0;
  long long length = pancakes.length();
    
  for ( long long i = 0 ; i < length ; i++ )
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
    position = ( ( long long ) pow( 2, floor( log2( position ) ) + 1 ) - 1 ) - position;
    result += 1; 
  } // while  
  
  result += position;  
  return result;
} // end GetNumOfTimes()






