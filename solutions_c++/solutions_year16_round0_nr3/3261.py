#include <bits/stdc++.h>

using namespace std;

long long fac[15];

bool isNotPrime(unsigned long long num) {
  for (int i = 2; i <= sqrt(num); i++) {
    if (num % i == 0) {
      return true;
    }
  }
  return false;
}

long long solve(unsigned long long num) {
  if (num % 2 == 0) {
    return 2;
  } else {
    for (int i = 3; i <= sqrt(num); i += 2) {
      if (num % i == 0) {
        return i;
      }
    }
  }
}

long long conv(int num) {
  if (num <= 1) {
    return num;
  }
  return conv(num >> 1) * 10 + (num % 2);
}

int main() {
  int t;
  cin >> t;
  cout << "Case #" << t << ":" << endl;
  int n, q;
  cin >> n >> q;
  bool done;
  for (int i = 32769; i <= 65535; i += 2) {
    if (q) {
      ostringstream cur;
      cur << conv(i);
      for (int j = 2; j <= 10; j++) {
        unsigned long long now = std::stoull(cur.str(), 0, j);
        if (isNotPrime(now)) {
          fac[j] = solve(now);
          done = true;
        } 
        else {
          done = false;
          break;
        }
      }
      if (done) {
        cout << conv(i);
        for (int j = 2; j <= 10; j++) {
          cout << " " << fac[j];
        }
        cout << endl;
        q--;
      }
    }
  }
  return 0;
}