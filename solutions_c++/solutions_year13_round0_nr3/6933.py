#include <iostream>
#include <string>
#include <sstream>
#include <cmath>

using namespace std;

bool ispalindromes( string str ) {
  int len = str.size();
  bool is = true;
  for(int i=0; i<len/2; i++) {
    if( str[i] != str[len-i-1] ) {
      is = false;
      break;
    }
  }
  return is;
}

int main() {
  int T,A,B;
  int t,a,b;
  cin >> T;
  for(t=1; t<=T; t++) {
    cin >> A >> B;

    a = (int)ceil(  sqrt(A) );
    b = (int)floor( sqrt(B) );

    //cout << "debug " << a << "," << b << endl;

    int result=0;
    for(int i=a; i<=b; i++) {
      stringstream ss;
      ss << i << " " << i*i;
      string str,str2;
      ss >> str >> str2;

      //cout << str << " " << str2 << endl;
      
      if( ispalindromes(str) ) {
	if( ispalindromes(str2) ) {
	  //cout << "debug " << str2 << endl;
	  result++;
	}
      }
    }
    cout << "Case #" << t << ": " << result << endl;
  }
}
