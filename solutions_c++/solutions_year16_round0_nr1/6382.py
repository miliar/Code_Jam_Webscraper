#include <iostream>
using namespace std;

bool digits[10] = {false};

void decomposeNumber(unsigned long n) {
  while (n > 0) {
    int digit = n % 10;
    n /= 10;

    digits[digit] = true;
  }
}

void solve(unsigned long n, int caseNum) {
  if (n * 1 == n * 2) {
    cout << "Case #" << caseNum << ": INSOMNIA\n";
    return;
  }

  for (int i = 0; i < 10; ++i) digits[i] = 0;
  bool allFound = false;

  int idx = 1;
  while (!allFound) {
    decomposeNumber(n * idx++);

    allFound = true;
    for (int i = 0; i < 10; ++i) {
      if (!digits[i]) allFound = false;
    }
  }

  cout << "Case #" << caseNum << ": " << n * (idx-1) << "\n";
}

int main() {
	int T;
	unsigned long n;
  
  cin >> T;
  for (int t = 0; t < T; ++t) {
    cin >> n;
    solve(n, t + 1);
  }
}