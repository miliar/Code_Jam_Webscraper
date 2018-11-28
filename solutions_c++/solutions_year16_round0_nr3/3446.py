#include<iostream>
#include<fstream>
#include<string>
#include<cmath>

using namespace std;

#define MAX_N 50000

int64_t t;
ifstream in("in.txt");
//ifstream in("C-small-attempt0.in");
//ifstream in("C-large.in");
ofstream out("out.txt");
int64_t primes[MAX_N];

void initPrimes() {
  int cnt = 2;
  primes[0] = 2;
  primes[1] = 3;

  int64_t i = 5;
  int j, m = 1, sum_div = 0;

  while(1) {
    for(j = 0; j < cnt; j++) {
      if(i % primes[j] == 0) {
        sum_div += 1;
        break;
      }
    }

    if(sum_div == 0) {
      primes[cnt] = i;
      cnt += 1;
      //cout << i << endl;
    }

    i += 2;
    sum_div = 0;

    if(cnt >= MAX_N) break;
  }
}

int64_t convert(int64_t *num, int64_t n, int64_t base) {
  int64_t sum = 0;

  for(int64_t i = n - 1; i >= 0; i--) {
    if(num[i] == 1) 
      sum += pow(base, n - i - 1);
  }

  return sum;
}

int64_t getDivider(int64_t n) {
  for(int i = 0; i < MAX_N; i++) {
      if(n != primes[i] && n % primes[i] == 0) return primes[i];
  }

  cout << "doesn't have: " << n << endl;
  return 0;
}

void cal(int64_t n, int j) {
  int64_t cnt = 0;

  int64_t num[32];
  for(int64_t i = 0; i < 32; i++) {
    num[i] = 0;
  }
  num[0] = 1;
  num[n - 1] = 1;
  int64_t bases[10];

  while(cnt != j) {
    cout << "2digits: " << endl;
    for(int64_t i = 0; i < n; i++) {
      cout << num[i];
    }
    cout << endl;

    bool isPrime = false;
    for(int64_t i = 0; i < 9; i++) {
      bases[i] = convert(num, n, i + 2);

      cout << "converted(" << i + 2 << "): " << bases[i] << endl;

      bool prime = true;
      for(int j = 0; j < MAX_N; j++) {
        if(bases[i] != primes[j] && bases[i] % primes[j] == 0) {
          prime = false;
          break;
        }
      }
      if(prime) {
        isPrime = prime;
      }

      if(isPrime) break;
    }

    if(!isPrime) {
      cnt += 1;
      for(int64_t i = 0; i < n; i++) {
        out << num[i];
        cout << num[i];
      }
      for(int64_t i = 0; i < 9; i++) {
        out << " " << getDivider(bases[i]);
        cout << " " << getDivider(bases[i]);
      }
      out << endl;
      cout << endl;
    }

    int64_t before = 1;
    for(int64_t i = n - 2; i >= 1; i--) {
      if(num[i] + before == 2) {
        num[i] = 0;
        before = 1;
      } else {
        num[i] = num[i] + before;
        before = 0;
      }
    }
  }
}

int main() {
  initPrimes();
  cout << "InitPrime" << endl;
  cout << primes[MAX_N - 1] << endl;

  in >> t;

  int64_t n, j;
  for(int64_t i = 0; i < t; i++) {
    in >> n >> j;

    out << "Case #" << i + 1 << ":" << endl;
    cal(n, j);
  }

}
