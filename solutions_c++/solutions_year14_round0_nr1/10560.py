#include <iostream>
using namespace std;

int main() {
   int numOfCases;
   int firstRow, secondRow;
   int arr1[4][4];
   int arr2[4][4];
   int firstMatch = 0;
   bool badResult = false;
   cin >> numOfCases;
   int cases = 1;
   while( cases <= numOfCases ) {
      cout << "Case #" << cases << ": ";
      cin >> firstRow;
      for( int i = 0; i < 4; i++ ) {
         for( int j = 0; j < 4; j++ ) {
            cin >> arr1[i][j];
         }
      }
      cin >> secondRow;
      for( int i = 0; i < 4; i++ ) {
         for( int j = 0; j < 4; j++ ) {
            cin >> arr2[i][j];
         }
      }
      for( int i = 0; i < 4; i++ ) {
         for( int j = 0; j < 4; j++ ) {
            //cout << arr1[i][j] << " ";
         }
         //cout << endl;
      }
      for( int i = 0; i < 4; i++ ) {
         for( int j = 0; j < 4; j++ ) {
            //cout << arr2[i][j] << " ";
         }
         //cout << endl;
      }
      firstMatch = 0;
      badResult = false;
      for( int i = 0; i < 4; i++ ) {
         for( int j = 0; j < 4; j++ ) {
            if( arr1[ firstRow-1 ][ i ] == arr2[ secondRow-1 ][ j ] ) {
               //cout << arr1[ firstRow-1 ][ i ] << endl;
               if( firstMatch ) {
                  badResult = true;
                  break;
               } else {
                  firstMatch = arr1[ firstRow-1 ][ i ];
               }
            }
            if( badResult )
               break;
         }
      }
      if( !firstMatch ) {
         cout << "Volunteer cheated!" << endl;
      } else if( !badResult ) {
         cout << firstMatch << endl;
      } else {
         cout << "Bad magician!" << endl;
      }
      cases++;
   }
   return 0;
}

            
   
