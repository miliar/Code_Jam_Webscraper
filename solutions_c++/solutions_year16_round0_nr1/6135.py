#include<iostream>

using namespace std;

bool notAll(bool v[]) {
  for (int i = 0; i < 10; i++) {
    if (!v[i]) {
      return true;
    }
  }
  return false;
}

void mark(bool v[], long n) {
  while (n != 0) {
    v[n % 10] = true;
    n /= 10;
  }
}

int main() {
  bool v[10];
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    long n;
    cin >> n;
    cout << "Case #" << t << ": ";
    if (n == 0) {
      cout << "INSOMNIA" << endl;
    } else {
      for (int i = 0; i < 10; i++) {
        v[i] = false;
      }
      long r = 0;
      mark(v, n);
      while (notAll(v)) {
        r += n;
        mark(v, r);
      }
      cout << r << endl;
    }
  }
  return 0;
}
