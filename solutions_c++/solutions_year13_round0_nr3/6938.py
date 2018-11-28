#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cmath>
#include <vector>

using namespace std;

bool isFair( int n ){
  vector<int> number;
  int i=10;
  while( n > 0 ){
       number.push_back( (n%i)*10/i );
       n = n - n%i;
       i = i*10;
  }
  int j;
  for( i=0, j=number.size()-1; i!=j ; i++, j-- ){ 
     if( number.at(i) != number.at(j) )
       return false;
     if( i == j+1 )
       return true;
  }
  return true;
}

bool isFairAndSquare(int n){
     int sqroot = (int) sqrt( n );
     if( sqroot*sqroot != n )
       return false;
     return (isFair( n ) && isFair( sqroot ));
}

int main(){
    string buff;
    fstream inFile, outFile;
    inFile.open ("codeIn.txt");
    outFile.open("codeOut.txt");
    getline( inFile, buff );
    int T = atof( buff.c_str() );
    int A, B, N;
    unsigned int sPos;
   for( int i=0; i < T; i++ ) {
       N=0;
       getline( inFile, buff );
       sPos = buff.find(" ");
       A = atof( (buff.substr(0, sPos+1)).c_str() );
       B = atof( (buff.substr(sPos)).c_str() );
       for( int n=A; n<=B; n++ ){
          if( isFairAndSquare( n ) ){
            N++;
          }
       }
       outFile << "Case #" << i+1 << ": " << N << endl;
    }
   return 0;
}
