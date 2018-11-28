#include <iostream>
#include <math.h>
#include "bigInt.h"

using namespace std;

BigInt::Rossi ComputeNum(int num[], int base, int N) {
  BigInt::Rossi res = BigInt::Rossi (0);
  BigInt::Rossi big_base (base);
  for (int i = 0; i < N; ++i) {
    res = (res * big_base + BigInt::Rossi(num[i]));
  }
  return res;
}

void FindNext(int* num, int N) {
  // Find last 0 from location 1 to N - 2.
  int last_zero = -1;
  for (int i = N - 2; i >= 1; --i) {
    if (num[i] == 0) {
      last_zero = i;
      break;
    }
  }
  num[last_zero] = 1;
  for (int i = last_zero + 1; i <= N - 2; ++i) {
    num[i] = 0;
  }
}

void PrintBitString(int num[], int N) {
  for (int i = 0; i < N; ++i) {
    cout << num[i];
  }
  cout << " ";
}

BigInt::Rossi FindFactor(BigInt::Rossi s) {
  BigInt::Rossi limit = BigInt::Rossi(1000);
  for (BigInt::Rossi i(2); i <= limit; ++i) {
    if (s % i == BigInt::Rossi(0)) {
      return i;
    }
  }
  return BigInt::Rossi(0);
}

int main(int argc, char** argv) {
  int T, N, J;
  cin >> T;
  cin >> N;
  cin >> J;
  cout << "Case #1:" << endl;
  int num[N];
  for (int i = 0; i < N; ++i ) {
    num[i] = 0;
  }
  num[0] = 1;
  num[N - 1] = 1;
  int num_found = 0;
  for (int i = 0; i < (int) pow(2.0, (double) (N - 2)); ++i) {
    BigInt::Rossi factors[11];
    int base = 2;
    for (; base <= 10; ++base) {
      // cout << "Computing number for base: " << base << endl;
      BigInt::Rossi s = ComputeNum(num, base, N);
      // cout << "Finding factor for base: " << base << endl;
      factors[base] = FindFactor(s);
      if (factors[base] == BigInt::Rossi(0)) break;
    }
    if (base == 11) {
      num_found++;
      PrintBitString(num, N);
      for (int i = 2; i <= 10; ++i) {
        cout << factors[i].toStrDec() << " ";
      }
      cout << endl;
    }
    if (num_found == J) break;
    FindNext(num, N);
  } 
  if (num_found < J) cout << "Cry cry cry" << endl;
  return 0;
}
