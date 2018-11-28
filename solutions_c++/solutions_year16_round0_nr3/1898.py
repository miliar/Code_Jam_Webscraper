#include <iostream>
#include <bitset>
#include <cmath>
#include <vector>
using namespace std;

long long divisor(long long jc) {
  for (long long i = 2; i <= sqrt(jc); ++ i) {
    if (jc % i == 0) return i;
  }
  return 1;
}

const int K = 32;

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cout << "Case #" << t << ":" << endl;
    int N, J;
    cin >> N >> J;
    int c = 0;
    long long M = 1L << (N - 2);
    for (long long i = 3; (i < M) && (c < J); i += 3) {
      //long long jc = M  + i + 1;
      long long jc = i;
      bitset<K> jcb = bitset<K>(jc);
      vector<long long> d(11, 1); 
      bool has_prime = false;
      for (int base = 2; !has_prime && (base <= 10); ++base) {
        long long jcc = 0;
        for (int i = 0; i < K; ++i) {
          jcc *= base;
          jcc += jcb[K - i - 1];
        }
        if (jcc % (base + 1) == 0) {
          d[base] = base + 1;
        } else {
          d[base] = 1;
          has_prime = true;
        }
        /*
        d[base] = divisor(jcc);
        if (d[base] == 1) has_prime = true;
        */
      }
      if (!has_prime) {
        cout << bitset<K>(2 * (M  + i) + 1);
        for (int base = 2; base <= 10; ++base) {
          cout << " " << d[base]; 
        }
        cout << endl;
        c++;
      } else {
        //cout << jc << endl;
      }
    }
  }
  return 0;
}
