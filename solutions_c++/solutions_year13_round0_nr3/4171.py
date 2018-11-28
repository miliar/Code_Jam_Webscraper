#include <iostream>
#include <vector>

using namespace std;

vector<long> base10(long x) {
  vector<long> result;
  while (x > 0) {
    result.push_back(x % 10);
    x /= 10;
  }
  return result;
}

bool fair(long x) {
  vector<long> digits = base10(x);
  bool result = true;
  for (long i = 0; i < digits.size()/2; i++) {
    if (digits[i] != digits[digits.size()-i-1]) result = false;
  }
  return result;
}

int main() {
  long T;
  cin >> T;
  for (long i = 0; i < T; i++) {
    long A, B;
    cin >> A >> B;
    long total = 0;
    long cand = 1;
    while (cand*cand < A) cand++;
    while (cand*cand <= B) {
      if (fair(cand) && fair(cand*cand)) {
        cout << cand*cand << endl;
        total++;
      }
      cand++;
    }
    cout << "Case #" << (i+1) << ": " << total << endl;
  }
}
