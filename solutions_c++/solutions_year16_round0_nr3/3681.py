#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <math.h>

using namespace std;

void print_vector(const vector<int>& v);
long horners_base(const vector<int>& v, int base);
long isPrime(long num);
vector<long> isJamcoin(const vector<int>&);

int main() {
  int T;
  cin >> T;
  set<int> primes;
  for(int k = 1; k <= T; k++) {
    int n,J;
    cin >> n >> J;
    // N : length of jamcoin
    // J : number of jamcoins required
    vector<int> num(n);
    for(int i = 0; i < n; i++) num[i] = 0;
    num[0] = 1; num[n - 1] = 1;
    int times = pow(2, n - 2);
    int count = 0;
    cout << "Case #" << k << ":" << endl;
    for(int i = 0; i < times; i++) {
      //print_vector(num);
      //cout << horners_base(num, 3) << endl;

      // TODO: LOGIC FOR EACH JAMCOIN of length n
      vector<long> is = isJamcoin(num);
      if(is[0] != -1) {
        print_vector(num);
        for(int i = 2; i < 11; i++) {
          cout << " " << is[i];
        }
        cout << endl;
        count++;
        if(count == J) break;
      }

      // END LOGIC

      int status[n-2] = {0};
      // always invert bit0
      if(num[n-1-1] == 0) {
        num[n-1-1] = 1;
      } else {
        // bit0 goes from 1 to 0
        status[n-1-1] = 1;
        num[n-1-1] = 0;
      }

      for(int j = n-2-1; j >= 1; j--) {
        if(status[j+1] == 1) {
          if(num[j] == 0) {
            num[j] = 1;
            break;
          } else {
            num[j] = 0;
            status[j] = 1;
          }
        }
      }
    }
  }
  return 0;
}

vector<long> isJamcoin(const vector<int>& v) {
  vector<long> factors(11);
  for(int base = 0; base < 11; base++) factors[base] = 0;
  for(int base = 2; base < 11; base++) {
    // for each base
    long num = horners_base(v, base);
    long is_prime = isPrime(num);
    if(is_prime == -1) {
      // it is prime. not a jam coin
      factors[0] = -1;
      break;
    } else {
      factors[base] = is_prime;
    }
  }

  return factors;
}

long horners_base(const vector<int>& v, int base) {
  long res = v[0];
  for(int i = 1; i < v.size(); i++) {
    res = res * base + v[i];
  }

  return res;
}

long isPrime(long num) {
  long lim = (long)ceil(sqrt(num));
  for(long i = 2; i < lim; i++) {
    if(num % i == 0) return i;
  }
  return -1;
}

void print_vector(const vector<int>& v) {
  for(int i = 0; i < v.size(); i++) cout << v[i];
}

// generate primes upto but not including N
/*void sieve(int N, set<int>& primes) {
  vector<int> list(N);
  for(int i = 0; i < N; i++) {
    list[i] = 1;
  }
  list[0] = list[1] = 0;

  for(int i = 2; i < N; i++) {
    for(int j = i * i; j < N; j += i) {
      list[j] = 0;
    }
  }

  for(int i = 0; i < N; i++) {
    if(list[i] == 1) primes.insert(i);
  }
}*/
