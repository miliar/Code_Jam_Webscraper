#include <iostream>
using namespace std;
bool done (bool flag[]) {
  for (int i = 0; i < 10; ++i) {
    if (flag[i] == false) {
      return false;
    }
  }
  return true;
}
void fill(bool flag[], unsigned long long N) {
  while (N > 0) {
    flag[N % 10] = true;
    N /= 10;
  }
}
int main() {
  int T = 0;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    bool flag[10];
    for (int count = 0; count < 10; ++count) {
      flag[count] = false;
    }
    unsigned long long N = 0;
    cin >> N;
    if (N == 0) {
      cout << "Case #" << i << ": INSOMNIA" << endl;
      continue;	
    }
    unsigned long long j = 1;
    unsigned long long N1 = N;
    while (N1 % 10 == 0) {
      flag[0] = true;
      N1 /= 10;
    }
    while (!done(flag)) {
      fill(flag, j * N1);
      ++j;    
    }
    cout << "Case #" << i << ": " << (j - 1) * N << endl;
  }
}
