#include <iostream>
#include <unordered_set>

using namespace std;

int solve(int current) {
  unordered_set<int> seen;
  int initial = current;
  while (seen.size() < 10) {
    int temp = current;
    while (temp > 0) {
      int digit = temp % 10;
      seen.emplace(digit);
      temp /= 10;
    }
    current += initial;
  }
  return current - initial;
}

int main() {
  int n;
  cin >> n;
  for (int i = 1; i <= n; i++) {
    int current;
    cin >> current;
    if (current == 0) {
      cout << "Case #" << i << ": INSOMNIA" << endl;
    } else {
      cout << "Case #" << i << ": " << solve(current) << endl;
    }
  }
}
