#include <iostream>
#include <vector>

using namespace std;

void solveCase() {
  int n;
  cin >> n;

  if (n == 0) {
    cout << "INSOMNIA";
    return;
  }

  bool seen[10] = {};
  int64_t number = n;

  while (true) {
    auto s = to_string(number);
    for (char c : s) {
      seen[c-'0'] = true;
    }
    bool done = true;
    for (int i = 0; i < 10; i++) {
      if (!seen[i]) {
        done = false;
        break;
      }
    }
    if (done) {
      cout << number;
      return;
    }
    number += n;
  }
}

#define NAME "A-large"
//#define NAME "A-small-attempt0"
//#define NAME "test"

int main() {
  freopen(NAME".in", "rt", stdin);
  freopen(NAME".out", "wt", stdout);
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    cout << "Case #" << i << ": ";
    solveCase();
    cout << endl;
  }
  return 0;
}
