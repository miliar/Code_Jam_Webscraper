#include <iostream>
using namespace std;

long calc(int N) {
  int flg = 0b0000000000;
  int a = N;
  while (1) {
    int num = a;
    while (num) {
      flg |= 1 << (num % 10);
      num /= 10;
    }
    if (flg == 0b1111111111) {
      break;
    }
    a += N;
  }
  return a;
}

int main() {
  int T, N;
  cin >> T;

  for (int i = 0; i < T; ++i) {
    cin >> N;
    cout << "Case #" << i + 1 << ": ";
    if (N) {
      cout << calc(N);
    } else {
      cout << "INSOMNIA";
    }
    cout << endl;
  }
}
