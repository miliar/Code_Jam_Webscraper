#include <iostream>
#include <vector>

using namespace std;

long long count(int N) {
  if (N == 0) return -1;
  long long num = N;
  int total = 10;
  vector<bool> digits(10, false);
  while (1) {
    long long tmp = num;
    while (tmp > 0) {
      if (!digits[tmp % 10]) {
        digits[tmp % 10] = true;
        total--;
        if (!total) return num;
      }
      tmp = tmp / 10;
    }
    num += N;
  }
  return -1;
}

int main() {
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    int N; 
    cin >> N;
    long long c = count(N);
    cout << "Case #" << i << ": ";
    if (c == -1) {
      cout << "INSOMNIA";
    } else
      cout << c;
    cout << endl; 
  }
  return 0;
}

