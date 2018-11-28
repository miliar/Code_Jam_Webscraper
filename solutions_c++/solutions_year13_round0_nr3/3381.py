#include <iostream>
#include <gmpxx.h>
#include <string>
using namespace std;

bool isPalindrome( mpz_class a ) {
   string s = a.get_str();
   int start = 0;
   int end = s.length() - 1;
   while( start < end ) {
      if( s[ start ] != s[ end ] )
         return false;
      start++;
      end--;
   }
   return true;
}
mpz_class getNumOfFSquareInts( mpz_class a, mpz_class b ) {
   mpz_class aSqrt = sqrt( a );
   mpz_class bSqrt = sqrt( b );
   mpz_class count( 0 );
   mpz_class tmp;
   tmp = aSqrt*aSqrt;
   if( isPalindrome( aSqrt ) && isPalindrome( tmp ) && tmp >= a ) {
      count = count + 1;
   }
   aSqrt = aSqrt + 1;
   while( aSqrt <= bSqrt ) {
      if( isPalindrome( aSqrt ) && isPalindrome( aSqrt*aSqrt ) )
         count = count + 1;
      aSqrt = aSqrt + 1;
   }
   return count;
}

int main() {
   int testCases;
   cin >> testCases;
   mpz_class a, b;
   int currCase = 1;
   while( currCase <= testCases ) {
      cin >> a >> b;
      cout << "Case #" << currCase << ": " << getNumOfFSquareInts( a, b ) << endl;
      currCase++;
   }
   return 0;
}
