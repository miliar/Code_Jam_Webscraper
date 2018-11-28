#include <iostream>
#include <map>
#include <vector>

using namespace std;

void solve(int n) {
  map<int, int> seen;
  map<int, int> digits;
  int next = 0;
  do {
    next += n;
    int curr = next;
    if (seen.find(curr) != seen.end()) {
      cout << "INSOMNIA";
      return;
    }
    seen[curr] = 1;
    while (curr > 0) {
      int dig = curr % 10;
      curr = curr / 10;
      digits[dig] = 1;
    }
  } while (digits.size() < 10);
  cout << next;
}

int main(int argc, char **argv) {
  int T, N;

  cin >> T;
  for (int i = 0; i < T; ++i) {
    cin >> N;
    cout << "Case #" << i+1 << ": ";
    solve(N);
    cout << endl;
  }
  return 0;
}

