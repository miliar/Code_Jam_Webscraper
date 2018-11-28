#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
using namespace std;

int main() {
  int T;
  cin >> T;
  long long int output[T];
  for(int i=0;i<T;i++) {
    unsigned long long int A, B, temp, count = 0;			
    long double sqrtRoot;
    cin >> A >> B;
    for(unsigned long long int j=A;j<=B;j++) {
      sqrtRoot = sqrt((long double) j);
      temp = (unsigned long long int) sqrtRoot;
      if((sqrtRoot - temp) == 0) {
	string str = static_cast<ostringstream*>( &(ostringstream() << j) )->str();
	bool isPalindrome = true, isSqrtRootPalindrome = true;
	int x = str.size() - 1;
	for(int k=0;k<str.size();k++) {
	  if(str.at(k) != str.at(x-k)) {
	    isPalindrome = false;
	    break;
	  }
	}
	str = static_cast<ostringstream*>( &(ostringstream() << temp) )->str();
	x = str.size() - 1;
	for(int k=0;k<str.size();k++) {
	  if(str.at(k) != str.at(x-k)) {
	    isSqrtRootPalindrome = false;
	    break;
	  }
	}
	if(isPalindrome == true && isSqrtRootPalindrome == true) 
	  count++;
      }
    }
    output[i] = count;
  }
  for(int i=0;i<T;i++)
    cout << "Case #" << i+1 << ": " << output[i] << endl;
  return 0;
}
