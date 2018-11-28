#include <cstdio>
#include <iostream>
#include <cassert>

using namespace std;

long long best (long long n, long long i) {
  if (i == n - 1) {
    return n - 1;
  }
  assert (n != 0);
  return best (n >> 1, (i + 1) / 2);
}
long long worst (long long n, long long i) {
  if (i == 0) {
    return 0;
  }
  return worst (n >> 1, (i - 1) / 2)  + (n >> 1);
}


void run(void) {
  long long N, P;
  cin >> N >> P;

  N = 1 << N;
  
  long long l = 0, r = N;
  while (l + 1 < r) {
    long long c = (l + r) >> 1;
    if (worst (N, c) < P) {
      l = c;
    } else {
      r = c;
    }
  }
  long long A = l;


  l = 0, r = N;
  while (l + 1 < r) {
    long long c = (l + r) >> 1;
    if (best (N, c) < P) {
      l = c;
    } else {
      r = c;
    }
  }
  long long B = l;
  cout << A << " " << B << "\n";
}

int main (void) {
  int test_n;
  scanf ("%d", &test_n);
  for (int test_i = 1; test_i <= test_n; test_i++) {
    printf ("Case #%d: ", test_i);
    run();
  }
  return 0;
}
