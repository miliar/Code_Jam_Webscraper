#include <algorithm>
#include <iostream>

using namespace std;

int main() {
  int t;
  cin >> t;
  for (int case_num = 1; case_num <= t; ++case_num) {
    int count[10] = {};
    int n;
    cin >> n;
    cout << "Case #" << case_num << ": ";
    if (n == 0) {
      cout << "INSOMNIA" << endl;
    } else {
      for (int i = 1; true; ++i) {
        int x = n * i;
        while (x > 0) {
          ++count[x % 10];
          x /= 10;
        }
        bool has_finished = true;
        for (int d = 0; d < 10; ++d) {
          if (count[d] == 0) {
            has_finished = false;
            break;
          }
        }
        if (has_finished) {
          cout << n * i << endl;
          break;
        }
      }
    }
  }
  return 0;
}
