#include <iostream>

using namespace std;

void count_digits(int counts[], int n) {
  while (n > 0) {
    counts[n % 10]++;
    n /= 10;
  }
}

bool finished(int counts[]) {
  for (int i = 0; i < 10; i++) {
    if (counts[i] == 0)
      return false;
  }

  return true;
}

int main() {
  int t;
  cin >> t;

  for (int i = 0; i < t; i++) {
    long n;
    cin >> n;
    int counts[10] = { 0 };
    long y = n;

    if (n == 0) {
      cout << "Case #" << i + 1 << ": INSOMNIA" << endl;
      continue;
    }

    while (!finished(counts)) {
      count_digits(counts, y);
      y += n;
    }
    cout << "Case #" << i + 1 << ": " << y - n << endl;
  }

  return 0;
}
