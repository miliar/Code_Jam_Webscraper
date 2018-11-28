#include <cstdlib>
#include <string>
#include <iostream>
#include <set>

#define I 2
#define J 3
#define K 4

#define LMAX 10000

using namespace std;

int mult[4][4] = {
  {1,  I,  J,  K},
  {I, -1,  K, -J},
  {J, -K, -1,  I},
  {K,  J, -I, -1}
};

int multiply(int a, int b) {
  if (a < 0 && b < 0) return mult[-a-1][-b-1];
  else if (a < 0) return -mult[-a-1][b-1];
  else if (b < 0) return -mult[a-1][-b-1];
  else return mult[a-1][b-1];
}

// Compute the full product, as well as update suffixes.
int product(int chars[LMAX], int suffixes[LMAX], int L) {
  int product = 1;
  for (int p=L-1; p>=0; p--) {
    product = multiply(chars[p], product);
    suffixes[p] = product;
  }
  return product;
}

// Return the value of n times the generator.
int repeat(int full, int n) {
  if (n <= 0) return 1;
  else if (full == 1) return 1;
  else if (full == -1 && n%2 == 0) return 1;
  else if (full == -1 && n%2 == 1) return -1;
  else if (n%4 == 0) return 1;
  else if (n%4 == 1) return full;
  else if (n%4 == 2) return -1;
  else if (n%4 == 3) return -full;
}

// Return the value of the suffix chars[p] * .. * chars[L*X].
int suffix(int full, int suffixes[LMAX], int L, int X, int p) {
  return multiply(suffixes[p%L], repeat(full, X-p/L-1));
}

int main() {
  // Number of cases.
  int N;
  cin >> N;

  // Array without repetitions.
  int chars[LMAX];
  int suffixes[LMAX];

  // For each test case.
  for (int i=1; i<=N; i++) {
    int L, X;
    cin >> L >> X;
    char c;
    for (int j=0; j<L; j++) {
      cin >> c;
      if (c == 'i') chars[j] = I;
      if (c == 'j') chars[j] = J;
      if (c == 'k') chars[j] = K;
    }

    // Compute full product and suffixes.
    int full = product(chars, suffixes, L);

    // Simple solution.
    bool OK = false;
    int valueI = 1, valueJ = 1, valueK = 1;
    for (int p=0; p<L*X-2 && !OK; p++) {
      valueI = multiply(valueI, chars[p%L]);

      if (valueI == I) {
        valueJ = 1;
        for (int q=p+1; q<L*X-1 && !OK; q++) {
          valueJ = multiply(valueJ, chars[q%L]);

          if (valueJ == J) {
            valueK = suffix(full, suffixes, L, X, q+1);
            if (valueK == K) OK = true;
          }
        }
      }
    }

    if (OK) cout << "Case #" << i << ": YES" << endl;
    else cout << "Case #" << i << ": NO" << endl;
  }

  return 0;
}