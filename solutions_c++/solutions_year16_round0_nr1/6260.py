#include <iostream>
using namespace std;

int   is_true(bool *tab) {
  for (size_t i = 0; i < 10; i++) {
    if (tab[i] == false)
      return true;
  }
  return false;
}

int main() {
  int t, n, k, tmp;
  bool tab[10];

  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cin >> n;
    if (n == 0)
      cout << "Case #" << i << ": INSOMNIA" << endl;
    else {
      for (size_t j = 0; j < 10; j++) {
        tab[j] = false;
      }
      k = 1;
      while (is_true(tab)){
        tmp = n * k++;
        while (tmp > 0) {
          tab[tmp % 10] = true;
          tmp /= 10;
        }
      }
      cout << "Case #" << i << ": " << n * (k - 1) << endl;
    }
  }
  return (0);
}
