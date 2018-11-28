#include <iostream>
#include <math.h>
#include <sstream>

using namespace std;

inline bool isSquare(double a) {
  double s = sqrt(a);
  if ( fabs(s*s-a) < 1e-5 ) return true;
  return false;
}
  
inline bool isPalindrome(double a) {
  stringstream s;
  s << a;
  string str;
  s >> str;
  size_t len = str.size();
  for ( size_t i=0; i < len/2; i++ )
    if ( str[i] != str[len-1-i] ) return false;
  return true;
}

int main()
{
  int T, rT = 0;
  cin >> T;
  while ( rT++ != T )
  {
    double a, b;
    long long counter = 0;
    cin >> a >> b;
    while ( a <= b )
    {
      if ( isSquare(a) && isPalindrome(a) && isPalindrome(sqrt(a)) )
        counter++;
      a += 1.0;
    }
    cout << "Case #" << rT << ": " << counter << endl;
  }
}
