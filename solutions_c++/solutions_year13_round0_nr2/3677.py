#include <iostream>
using namespace std;

bool checkFeasibility( int **a, int noOfRows, int noOfCols ) {
   bool isFeasible = true;
   int curr;
   for( int i = 0; i < noOfRows; i++ ) {
      for( int j = 0; j < noOfCols; j++ ) {
         curr = a[ i ][ j ];
         for( int k = 0; k < noOfRows; k++ ) {
            if( curr < a[ k ][ j ] ) {
               isFeasible = false;
               break;
            }
         }
         if( !isFeasible ) {
            int k;
            for( k = 0; k < noOfCols; k++ ) {
               if( curr < a[ i ][ k ] )
                  break;
            }
            if( k == noOfCols )
               isFeasible = true;
         }
         if( !isFeasible )
            return false;
      }
   }
   return true;
}

int main() {
   int testCases;
   cin >> testCases;
   int noOfRows, noOfCols;
   int currCase = 1;
   while( currCase <= testCases ) {
      cin >> noOfRows >> noOfCols;
      int **a = new int*[ noOfRows ];
      for( int i = 0; i < noOfRows; i++ ) {
         a[ i ] = new int[ noOfCols ];
         for( int j = 0; j < noOfCols; j++ ) {
            cin >> a[ i ][ j ];
         }
      }
      if( checkFeasibility( a, noOfRows, noOfCols ) )
         cout << "Case #" << currCase << ": YES" << endl;
      else
         cout << "Case #" << currCase << ": NO" << endl;
      delete( a );
      currCase++;
   }
   return 0;
}
