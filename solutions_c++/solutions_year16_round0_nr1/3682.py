#include <iostream>
#include <string>

using namespace std;

// separate digits and mark them as seen
void check_digits(int x, bool digits_seen[])
{
  if (x >= 10) {
    check_digits(x / 10, digits_seen);
  }
  digits_seen[x % 10] = true;
}

int count_sheep(int n, int current_n, int mult, bool digits_seen[]) {
  check_digits(current_n, digits_seen);
  // check if all digits have been seen
  for (int i = 0; i < 10; i++) {
    if (!digits_seen[i]) {
      break;
    }
    if (i == 9) {
      return current_n;
    }
  }
  return count_sheep(n, mult * n, mult + 1, digits_seen);
}

int main() {
  int t, n;
  bool digits_seen[10] = {false};
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cin >> n;
    cout << "Case #" << i << ": " ;
    if (n == 0) {
      cout << "INSOMNIA" << endl;
    }
    else {
      cout << count_sheep(n, n, 2, digits_seen) << endl;
    }

    for (int i = 0; i < 10; i++) {
      digits_seen[i] = false;
    }
  }
}