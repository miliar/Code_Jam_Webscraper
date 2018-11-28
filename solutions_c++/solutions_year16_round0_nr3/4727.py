#include <iostream>
#include <cmath>

using namespace std;

unsigned long long checkPrime(unsigned long long number) {
    if (number == 2)
        return true;
    if (number == 3)
        return true;
    if (number % 2 == 0)
        return false;
    if (number % 3 == 0)
        return false;

    int i = 5;
    int w = 2;

    while (i * i <= number) {
        if (number % i == 0)
            return false;

        i += w;
        w = 6 - w;
    }
    return true;
}

unsigned long long getNonTrivialDivisor(unsigned long long number) {
    if (checkPrime(number)) {
        return 0;
    }
    unsigned long long divisor = 2;
    while (number % divisor > 0 && divisor < number) {
        divisor++;
    }
    
    if (divisor == number) {
        return 0;
    } else {
        return divisor;
    }
}

int analyze(bool *digits, int length) {
    unsigned long long divisors[9];
    unsigned long long numberInBinary;
    for (int i = 2; i <= 10 ; i++) {
        unsigned long long number = 0;
        for (int j = 0; j < length; j++) {
            number += digits[length-1-j] * std::pow(i, j);
        }
    
        unsigned long long divisor = getNonTrivialDivisor(number);
        if (divisor == 0) {
            return 0;
        }
        divisors[i-2] = divisor;
        numberInBinary = number;
    }
    
    cout << numberInBinary << " ";
    for (int i = 2; i <= 10; i++) {
        cout << divisors[i-2] << " ";
    }
    cout << endl;
    return 1;
}

void solveDigits(bool *digits, int length, int remaining) {
    for(unsigned long long i = 0; i < pow(2, length-2); i++) {
       for (int j = 0; j < length - 2; j ++) {
            int digit = (i / std::pow(2,j));
            digits[length-1-j-1] = digit % 2;
        }
        remaining -= analyze(digits, length);
        if(remaining == 0)
            return;
    }
}

int main() {
  int t, n, j; 
  cin >> t;
  
  for (int i = 1; i <= t; ++i) {
    cin >> n >> j;
    
    bool digits[n];
    std::fill(digits, digits+n, false);
    digits[0] = true;
    digits[n-1] = true;
    
    cout << "Case #" << i << ": " << endl;
    solveDigits(digits, n, j);    
  }
  
  return 0;
}
