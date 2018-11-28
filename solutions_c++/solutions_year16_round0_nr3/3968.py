#include <iostream>
#include <cstdio>
#include <limits>
#include <vector>
#include <math.h>
#include <cstring>

using namespace std;

void binary(unsigned int val, int N)
{
   unsigned int mask = 1;
   mask <<= (N - 1);
   for(int i = 0; i < N; i++)
   {
      if( (val & mask) == 0 ) {
         cout << '0';
      } else{
         cout << '1';
       }
      mask >>= 1;
   }
}

// binary to base number
unsigned long long convert(unsigned int number, int base, int N)
{
  int i = 0;
  unsigned long long answer = 0;
  unsigned int copy = number;
  while (i < N) 
  {
    int digit = copy & 1;
    answer += (unsigned long long) (pow(base, i) * digit);
    copy >>= 1; 
    i++;
  }
  return answer;
}

// return 1 if not found
unsigned int getDivisor(unsigned long long number)
{
  unsigned int answer = 1;
  for (unsigned int i = 2; i < sqrt(number); i++) {
    if (number % i == 0) {
      answer = i;
      break;
    }
  }
  return answer;
}

bool isPrime(int number)
{
  if (number == 2 || number == 3) {
    return true;
  }
  if (number < 2 || number % 2 == 0) {
    return false;
  }
  if (number < 9) {
    return true;
  }
  if (number % 3 == 0) {
    return false;
  }
  int r = (int) pow(number, 0.5);
  int f = 5;
  while (f <= r) {
    if (number % f == 0) {
      return false;
    }
    if (number % (f+2) == 0) {
      return false;
    }
    f += 6;
  }
  return true;
}

bool jamcoin(unsigned int number, int &N, int &J)
{
  vector<unsigned int> divisors;
  for (int base = 2; base <= 10; base++) {
    unsigned long long val = convert(number, base, N);
    if (J <= 0 || isPrime(val)) {
      return false;
    }
    unsigned int divisor = getDivisor(val);
    // val is not prime and has non-trivial divisor
    if (divisor != 1) {
      divisors.push_back(divisor);
    }
  }
  // print answers
  if (divisors.size() == 9) {
    binary(number, N);
    for (int i = 0; i < divisors.size(); i++) {
      cout << " " << divisors[i];
    }
    cout << endl;
    J--;
    return true;
  }
  return false;
}

// number should not be prime in any base
// jamcoin should exists in each base => total 9
// jamcoin := nontrivial divisor
void solve(int &N, int &J)
{
  unsigned int number = 1;
  for(int i = 1; i < N; i++) {
    number <<= 1;
    number |= 1;
  }
  unsigned int smallest = 1;
  unsigned int mask = 1 << (N - 1);
  smallest |= mask;
  int incr = 2;
  while (number >= smallest && J > 0) {
    bool success = jamcoin(number, N, J);
    if (!success) {
      incr += 10;
    } else{
      incr = 2;
    }
    number -= incr;
  }
}

int main(int argc, char *args[]) {
  if (argc == 2 && strcmp(args[1], "small") == 0) {
    freopen("small.in", "rt", stdin);
    freopen("small.out", "wt", stdout);
  }
  else if (argc == 2 && strcmp(args[1], "large") == 0) {
    freopen("large.in", "rt", stdin);
    freopen("large.out", "wt", stdout);
  }
  else {
    freopen(args[1], "rt", stdin);
    freopen("a.out", "wt", stdout);
  }
  int T, N, J;
  cin >> T;
  for (int i = 1; i <= T; i++)
  {
    cin >> N >> J;
    printf("Case #%d: ", i);
    cout << endl;
    // solve
    solve(N, J);
  }
}