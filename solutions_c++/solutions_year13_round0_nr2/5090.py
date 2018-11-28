#include <iostream>
#include <vector>
#include <stdio.h>
#include <string.h>
#include <fstream>

using namespace std;

int arrVisited[ 100 ][ 100 ];
int matrix[ 100 ][ 100 ];
int ROWSIZE;
int COLSIZE;

bool recurse( int row, int col, int curVal )
{
  bool isPossible( true );
  for( int i = row - 1; i >= 0; --i ) {
    if( curVal >= matrix[ i ][ col ] ) {
      if( arrVisited[ row ][ col ] > 0 )
        return true;
      else if( arrVisited[ row ][ col ] < 0 )
        return false;
      continue;
    }
    isPossible = false;
    break;
  }//for( i );
  for( int i = row + 1; i < ROWSIZE; ++i ) {
    if( curVal >= matrix[ i ][ col ] ) {
      if( arrVisited[ row ][ col ] > 0 )
          return true;
      else if( arrVisited[ row ][ col ] < 0 )
        return false;
      continue;
    }
    isPossible = false;
    break;
  }//for( i );
  if( isPossible ) {
    arrVisited[ row ][ col ] = 1;
    return true;
  }//if();
  isPossible = true;
  for( int i = col - 1; i >= 0; --i ) {
    if( curVal >= matrix[ row ][ i ] ) {
       if( arrVisited[ row ][ col ] > 0 )
          return true;
      else if( arrVisited[ row ][ col ] < 0 )
        return false;
      continue;
    }
    isPossible = false;
    break;
  }//for( i );
  for( int i = col + 1; i < COLSIZE; ++i ) {
    if( curVal >= matrix[ row ][ i ] ) {
       if( arrVisited[ row ][ col ] > 0 )
          return true;
      else if( arrVisited[ row ][ col ] < 0 )
        return false;
      continue;
    }
    isPossible = false;
    break;
  }//for( i );
  if( isPossible ) {
    arrVisited[ row ][ col ] = 1;
  }else {
    arrVisited[ row ][ col ] = -1;
  }
  return isPossible;
}


int main()
{
  unsigned numOfTestCases( 0 );
  vector< bool > finalResult;
  cin >> numOfTestCases;
  for( unsigned i = 0; i < numOfTestCases; ++i ) {
    memset( arrVisited, 0, 100*100*sizeof( arrVisited[ 0 ][ 0 ] ) );
    memset( matrix, 0, 100*100*sizeof( matrix[ 0 ][ 0 ] ) );
    ROWSIZE = 0;COLSIZE = 0;
    cin >> ROWSIZE;
    cin >> COLSIZE;
    for( int j = 0; j < ROWSIZE; ++j ) {
      int element( 0 );
      for( int k = 0; k < COLSIZE; ++k ) {
        cin >> element;
        matrix[ j ][ k ] = element;
      }//for( k );
    }//for( j );
    bool tempResult( false );
    for( int j = 0; j < ROWSIZE; ++j ) {
      for( int k = 0; k < COLSIZE; ++k ) {
        if( j == 9 && k == 5 )
          cout<<"I am here"<<endl;
        tempResult = recurse( j, k, matrix[ j ][ k ] );
        if( ! tempResult ) break;
      }//for( k );
      if( ! tempResult ) break;
    }//for( j );
    finalResult.push_back( tempResult );
  }//for( i );
  
  ofstream myfile;
  myfile.open ("D:\\JunkCoding\\JunkStuffs\\Junk_Codes\\GooggleCodeJam2013\\GooggleCodeJam2013\\GooggleCodeJam2013\\LargeLawnOwerOP.txt");
  for( unsigned k = 0; k < finalResult.size(); ++k ) {
     if( finalResult[ k ] )
      myfile<<"Case #"<<k+1<<": "<<"YES"<<endl;
    else
      myfile<<"Case #"<<k+1<<": "<<"NO"<<endl;
  }
  return 0;
}