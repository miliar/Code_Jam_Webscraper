// compilation command: c++ --std=c++11 --stdlib=libc++ p3.cpp
#include <iostream>
#include <math.h>
#include <tuple>
#include <list>
using namespace std;

#define BASE 10

class Digits {
public:
  int sum;
  list<int> d;
  Digits(int x);
  Digits(Digits *digits, int next);
  void print();
  float palindrome(int num_digits);
};
Digits::Digits(int x) {
  sum = x * x;
  d.push_front(x);
}
Digits::Digits(Digits *digits, int next) {
  list<int> l (digits->d);
  d = l;
  sum = digits->sum;
  d.push_back(next);
  sum += next * next;
}
void Digits::print() {
  cout << "Sum: " << sum << " D:";
  
  for (list<int>::iterator it=d.begin(); it != d.end(); ++it)
    cout << ' ' << *it;
  cout << '\n';
}

float Digits::palindrome(int num_digits) {
  bool even = num_digits == 2 * (num_digits / 2);
  float x = 0;
  int power = num_digits - 1;
  for (list<int>::iterator it=d.begin(); it != d.end(); ++it) {
    x = x + (float (*it)) * pow(BASE, power);
    power--;
  }
  for (list<int>::reverse_iterator it=d.rbegin(); it != d.rend(); ++it) {
    if ((it == d.rbegin()) && (!even)) {
    } else {
      x = x + (float (*it)) * pow(BASE, power);
      power--;
    }
  }
  return x;
}

// This comes up with palindromes for which the square is also a palindrome
class FairSquare {
  list<Digits*> digits;
  void filter();
public:
  int num_digits;
  FairSquare();
  FairSquare(int n);
  void print();
  void addDigit();
  int num();
  list<float> enumerate();
};

list<float> FairSquare::enumerate() {
  list<float> l;
  for (list<Digits *>::iterator it=digits.begin(); it != digits.end(); ++it) {
    Digits *digs = *it;
    l.push_back(digs->palindrome(num_digits));
  }
  return l;
}

int num_distint_digits(int num_digits) {
  return num_digits / 2;
}

bool pred(Digits *digs) {
  int back = digs->d.back();
  return (digs->sum + back * back >= BASE);
}

void FairSquare::filter() {
  // remove ones that are too large now
  digits.remove_if(pred);
  // go through and update sums
  for (list<Digits *>::iterator it=digits.begin(); it != digits.end(); ++it) {
    Digits *digs = *it;
    int back = digs->d.back();
    digs->sum = digs->sum + back * back;
  }
}

void FairSquare::addDigit() {
  num_digits++;
  bool even = num_digits == 2 * (num_digits / 2);
  if (even) {
    // we just became even, the last unique digit is now doubled
    this->filter();
  } else {
    // we just became odd and now have another unique digit. We need to
    // iterate through all digits, and try to add 0, 1, and 2 if we
    // can.

    list<Digits*> new_digits;
    for (list<Digits *>::iterator it=digits.begin(); it != digits.end(); ++it) {
      Digits *digs = *it;
      for (int next = 0; next < 3; next++) {
	if (digs->sum + next * next < BASE) {
	  // cout << "Can add " << next << "\n";
	  new_digits.push_back(new Digits(digs, next));
	}
      }
    }
    digits = new_digits;
  }
}

FairSquare::FairSquare(int n) {
  num_digits = 1;
  digits.push_back(new Digits(1));
  digits.push_back(new Digits(2));
  digits.push_back(new Digits(3));
  for (int i = n ; i > 1 ; i--) {
    this->addDigit();
  }
}

int FairSquare::num() {
  return this->digits.size();
}
void FairSquare::print() {
  cout << "N Digits: " << num_digits << "\n";
  for (list<Digits*>::iterator it=digits.begin(); it != digits.end(); ++it) 
    (*it)->print();
}

int numFairSquaresWithNDigits(int n) {
  bool even = n == 2 * (n / 2);  
  if (even) return 0;
  FairSquare *fsq = new FairSquare(n / 2 + 1);
  return fsq->num();
}

int numPalindromes(int n_digits) {
  FairSquare *fsq = new FairSquare(n_digits);
  return fsq->num();
}

int numDigits(double n) {
  return floor(log(n)/log(10))+1;
}

int numFairSquaresBetween(float start_, float stop_) {
  float start = pow(start_, 0.5);
  float stop = pow(stop_, 0.5);
  int count = 0;
  
  //number of palindromes with the same digits as start that are greater than it
  int n_of_start = numDigits(start);
  // cout << "n of " << start << ": " << n_of_start << "\n";
  FairSquare *fsq = new FairSquare(n_of_start);
  list<float> palindromes = fsq->enumerate();
  for (list<float>::iterator it=palindromes.begin(); it != palindromes.end(); ++it) {
    // cout << *it << "\n";
    if ((*it >= start) && (*it <= stop)) count++;
  }
  // cout << "After start: " << count << "\n";

  //number of palindromes with the same digits as stop that are less than it
  int n_of_stop = numDigits(stop);
  if (n_of_stop > n_of_start) {
    // cout << "n of " << stop << ": " << n_of_stop << "\n";
    fsq = new FairSquare(n_of_stop);
    palindromes = fsq->enumerate();
    for (list<float>::iterator it=palindromes.begin(); it != palindromes.end(); ++it) {
      // cout << *it << "\n";
      if (*it <= stop) count++;
    }
    // cout << "After stop: " << count << "\n";

    for (int i = n_of_start + 1; i < n_of_stop; i++) {
      count += numPalindromes(i);
      cout << "After " << i << ": " << count << "\n";
    }
  }

  return count;
}

void oneTest(int n) {
  string line;
  float start, stop;
  scanf("%f %f\n", &start, &stop);
  cout << "Case #" << n << ": " << numFairSquaresBetween(start, stop) << "\n";  
}

int main() {
  int numTests;
  string empty;
  cin >> numTests; getline(cin, empty);
  for (int n = 0; n < numTests; n++) {
    oneTest(n+1);
  }
}
