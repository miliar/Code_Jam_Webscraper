#include <iostream>
#include <vector>
using namespace std;

void update_flag(long num, vector<bool> &flags) {
  while (num > 0) {
    flags[num % 10] = true;
    num /= 10;
  }
}

int main() {
  int n;
  cin >> n;
  for (int i = 1; i <= n; ++i) {
    cout << "Case #" << i << ": ";
    int k;
    cin >> k;
    if (k == 0) {
      cout << "INSOMNIA" << endl;
      continue;
    }
    vector<bool> flags(10, false);
    long now = k;
    for (int j = 0; j < 100; j++) {
      update_flag(now, flags);
      bool found = true;
      for (int d = 0; d < 10; d++) {
        if (!flags[d]) {
          found = false;
          break;
        }
      }
      if (found) {
        cout << now << endl;
        break;
      }
      now += k;
    }
  }
}
