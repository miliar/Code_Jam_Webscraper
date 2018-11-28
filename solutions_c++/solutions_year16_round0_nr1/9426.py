#include <iostream>

#define BASE	10

using namespace std;

int main () {
  int T, d;
  bool digits[10];
  signed long long int number, k, tmpNumber, inputNumber, tmpDigit;
  
  cin >> T;
  
  for (int t = 1; t <= T; ++t) {
    for (int i = 0; i < BASE; ++i) {
      digits[i] = false;
    }
    
    cin >> inputNumber;
    number = inputNumber;
    
    if (number == 0) {
      cout << "Case #" << t << ": INSOMNIA" << endl;      
    } else {
      d = 0;
      while(d < 10) {
	tmpNumber = number;
	while(tmpNumber > 0) {
	  tmpDigit = tmpNumber % 10;
	  if (digits[tmpDigit] == false) {
	    ++d;
	    digits[tmpDigit] = true;
	  }
	  tmpNumber /= 10;
	}
	if (d < 10) number += inputNumber;
      }
      
      cout << "Case #" << t << ": " << number << endl;
    }
  }
  
  return 0;
}