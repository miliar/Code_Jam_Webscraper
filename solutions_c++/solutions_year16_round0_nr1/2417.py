#include <bits/stdc++.h>

using namespace std;

bool seenDigits[10];

bool seeNumber(long long num) {
  while (num) {
    seenDigits[num % 10] = true;
    num /= 10;
  }

  for (int i = 0; i < 10; i++) {
    if (!seenDigits[i]) {
      return false;
    }
  }

  return true;
}

template <typename T>
void answer(int caseNum, T answer) {
  cout << "Case #" << caseNum << ": " << answer << endl;
}

void solve(int caseNum)  {
  long long n;
  cin >> n;

  if (n == 0) {
    answer(caseNum, "INSOMNIA");
    return;
  }

  fill(seenDigits, seenDigits + 10, false);

  for (int i = 1; i < 10000000; i++) {
    if (seeNumber(n * i)) {
      answer(caseNum, n * i);
      return;
    }
  }

  cerr << "No answer found :(" << endl;
  answer(caseNum, "INSOMNIA");
}

int main() {
  int t;
  cin >> t;

  for (int i = 0; i < t; i++) {
    solve(i + 1);
  }
}
