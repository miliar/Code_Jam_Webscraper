#include <bits/stdc++.h>

using namespace std;

bool seen[10];

void f(long long j) {
  while (j > 0) {
    seen[j % 10] = true;
    j /= 10;
  }
}

int main() {
  int N; cin >> N;
  for (int i = 0; i < N; i++) {
    int x; cin >> x;
    bool good = false;
    memset(seen, 0, sizeof(seen));
    if (x == 0) {
      cout << "Case #" << (i + 1) << ": INSOMNIA" << endl;
      continue;
    }
    long long k = x;
    while (!good) {
      good = true;
      f(k);
      for (int j = 0; j < 10; j++) {
        good = good & seen[j];
      }
      k += x;
    }

    cout << "Case #" << (i + 1) << ": " << (k - (long long)x) << endl;
  }
  return 0;
}

