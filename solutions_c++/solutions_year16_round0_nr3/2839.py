#include <string>
#include <fstream>
#include <iostream>
#include <istream>
#include <sstream>
#include <functional>
#include <numeric>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

bool checkPrime(unsigned long long n, int &divider) {
  int max = (int)sqrt(n);
  int i = 2;
  for (; i != max && n % i; ++i);

  if (i == max) return true;
  divider = i;
  return false;
}

unsigned long long toBase(bool *a, int N, int b) {
  unsigned long long bb = 1;
  unsigned long long ret = 0;
  for (int i = 0; i != N; ++i) {
    ret += a[i] * bb;
    bb *= b;
  }
  return ret;
}

string aToStr(bool *a, int N) {
  char ar[35] = { 0, };
  for (int i = 0; i != N; ar[i] = a[N - i - 1] + '0', ++i);
  return string(ar);
}

bool valid(bool *a, int N, string &str) {
  for (int b = 2; b != 11; ++b) {
    unsigned long long n = toBase(a, N, b);
    int divider;
    bool tmp = checkPrime(n, divider);
    if (tmp) return false;

    str += " " + to_string(divider);
  }
  return true;
}

void convert(unsigned int n, int N, bool *a) {
  for (int i = 0; i != N; ++i) {
    a[i + 1] = (n >> i) & 1;
  }
}

int main() {
  int T;
  cin >> T;

  for (int t = 0; t != T; ++t) {
    int N, J;
    cin >> N >> J;

    unsigned int i = 0;

    bool a[32] = { 0, };
    a[0] = a[N - 1] = 1;

    cout << "Case #" << t + 1 << ":" << endl;

    int count = 0;
    while (count != J)
    {
      convert(i, N - 2, a);

      string str = aToStr(a, N);
      bool tmp = valid(a, N, str);
      if (tmp) {
        cout << str << endl;
        ++count;
      }
      ++i;
    }
  }

  return 0;
}