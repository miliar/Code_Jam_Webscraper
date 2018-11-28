#include <algorithm>
#include <bitset>
#include <iostream>
#include <cmath>
#include <string>
#include <vector>
using namespace std;

vector<int> vPrimes;
int maxChecked = 0;

void primeList(int n) {
  if (maxChecked < n) {
    for (int i=maxChecked+1; i<=n; i++) {
      bool isPrime = true;
      for (int j=2; j*j<=i; j++) {
        if (i%j==0) {
          isPrime = false;
          break;
        }
      }
      if (isPrime) {
        vPrimes.push_back(i);
        // cout << i << endl;
      }
    }
    maxChecked = n;
  }
}

long interpret (string str, int base) {
  long digit = 0;
  for (int i = 0; i < str.size(); i++) {
    int ia = str[str.size()-i-1] - '0';
    digit += ia * pow(base,i);
  }
  return digit;
}

int findDivisor(int num) {
  for (int i = 2; i < num; i++) {
    if (num%i==0) {
      return i;
    }
  }
  return -1;
}

int bestPrime(long n) {
  if (n == 1) {
    return -1;
  }
  if (n == 3) {
    return -1;
  }
  if (n % 2 == 0) {
    return 2;
  }
  if (n % 3 == 0) {
    return 3;
  }
  long i = 5;
  long w = 2;
  while (i * i <= n) {
    if (n % i == 0) {
      return i;
    }

    i += w;
    w = 6 - w;
  }
  return -1;
}

int main() {
  cout << "Case #1:" << endl;
  primeList(100);
  string str = "1001";
  int found = 0;
  int next = 0;
  while (found < 50) {
    int test = (next << 1);
    test = test | (1 << 15);
    test = test | (1);
    str = bitset< 16 >( test ).to_string();
    //cout << str << endl;
    bool NonePrime = true;
    std::vector<int> divs;
    for (int i = 2; i <= 10; i++) {
      long digit = interpret(str, i);
      int divisor = bestPrime(digit);
      if (divisor > 0) {
        divs.push_back(divisor);
      } else {
        NonePrime = false;
        break;
      }
    }
    if (NonePrime) {
      found++;
      cout << str << " ";
      for (int i = 0; i < divs.size(); i++) {
        cout << divs[i] << " ";
      }
      cout << endl;
    }
    next++;
  }
  return 0;
}
