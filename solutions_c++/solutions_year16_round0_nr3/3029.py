#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

long transform_into_basis(long n, int base) {
  long result = 0;
  int exponent = 0;
  int coefficient = 0;
  while (n > 0) {
    coefficient = n % 2;
    n /= 2;
    result += coefficient * pow(base, exponent++);
  }
  return result;
}

string base2(long n) {
  string s;
  while (n > 0) {
    if (n % 2 == 1)
      s += '1';
    else
      s += '0';
    n /= 2;
  }
  reverse(s.begin(), s.end());
  return s;
}

int main() {

  ifstream fin("C-small-attempt0.in");
  ofstream fout("C-small-attempt0.out");

  fout << "Case #1: " << endl;
  
  int T;
  fin >> T;

  int N, J;
  fin >> N >> J;

  long candidate_jamcoin = pow(2, N - 1) + 1;

  vector<int> primes;
  const int MILLION = 1000000;

  // Sieve of Eratosthenes
  // upper bound determined by working precomputation
  // could also build up everytime the largest prime gets smaller than sqrt(candidate_jamcoin) in some base
  vector<bool> is_prime = vector<bool>(MILLION, true);
  for (int n = 2; n < sqrt(MILLION); n++) {
    if (is_prime[n]) {
      primes.push_back(n);
      for (int k = n * n; k <= MILLION; k += n)
	is_prime[k] = false;
    }
  }
    
  while (J > 0) {
    bool is_jamcoin = true;
    for (int base = 2; base <= 10 && is_jamcoin; base++) {
      long jc_in_base = transform_into_basis(candidate_jamcoin, base);

      is_jamcoin = false;
      for (int & p : primes)
	if (jc_in_base % p == 0) {
	  is_jamcoin = true;
	  break;
	}
    }

    if (is_jamcoin) {
      fout << base2(candidate_jamcoin);      
      for (int base = 2; base <= 10; base++) {
	long jc_in_base = transform_into_basis(candidate_jamcoin, base);
	for (int & p : primes) {
	  if (jc_in_base % p == 0) {
	    fout << " " << p;
	    break;
	  }
	}
      }
      fout << endl;
      J--;
    }
    
    candidate_jamcoin += 2;
  }
  
  return 0;
}
