#include <cstdlib>
#include <string>
#include <iostream>
#include <set>

using namespace std;

bool digits[10];

void resetDigits() {
    for (int d=0; d<10; d++)
        digits[d] = false;
}

bool allDigits() {
    unsigned int d;
    for (d=0; d<10 && digits[d]; d++);
    return d == 10;
}

void checkDigits(unsigned long n) {
    do {
        digits[n % 10] = true;
        n = n / 10;
    } while (n > 0);
}

int main() {
  // Number of cases.
  int N;
  unsigned long M;
  unsigned long P;
  cin >> N;

  // For each test case.
  for (int i=1; i<=N; i++)
  {
    cin >> M;
    P = M;

    if (M == 0) {
        cout << "Case #" << i << ": INSOMNIA" << endl;
        continue;
    }

    resetDigits();
    checkDigits(P);

    while (!allDigits()) {
        P += M;
        checkDigits(P);
    }

    cout << "Case #" << i << ": " << P << endl;
  }

  return 0;
}
