#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <set>

using namespace std;

set<int> get_digits(int n) {
  set<int> digits;
  while (n > 9) {
    digits.insert(n % 10);
    n = n / 10;
  }
  digits.insert(n);
  return digits;
}

void solve(int n) {
  if (!n) {
    cout << "INSOMNIA";
    return;
  }

  set<int> seen;
  int current = n;
  while (seen.size() != 10) {
    set<int> digits = get_digits(current);
    for (set<int>::iterator it = digits.begin(); it != digits.end(); ++it)
      seen.insert(*it);
    current += n;
  }

  cout << current - n;
}

int main (int argc, char **argv) {
  int n_test_cases;
  if (scanf("%d", &n_test_cases) != 1) return 1;

  for (int i = 1; i <= n_test_cases; i++) {
    int n;
    if (scanf("%d", &n) != 1) return 3;
    cout << "Case #" << i << ": ";
    solve(n);
    cout << endl;
  }
}

