#include <iostream>
using namespace std;

int main() {
  unsigned int t, n, j, digits;
  bool d[10];
  cin >> t;

  for (int i = 1; i <= t; ++i) {
    cin >> n;
    if (n != 0) {
        j = 0;
        digits = 0;
        for (int m = 0; m < 10; m++) { d[m] = false; }
        for (unsigned int k; digits < 10;) {
            j++;
            k = n * j;
            // if (n * j < n * (j - 1)) {
            //     cout << "n, j: " << n << ", " << j << endl;
            // }
            // cout << "k: " << k << endl;
            while (k != 0) {
                // cout << k%10;
                if (!d[k%10]) {
                    // cout << " *";
                    d[k%10] = true;
                    digits++;
                }
                // cout << endl;
                k = k / 10;
            }
        }
        // if (j > 70 || t < 101)
        cout << "Case #" << i << ": " << n*j /*<< ", " << j*/ << endl;
    } else {
        cout << "Case #" << i << ": " << "INSOMNIA" << endl;
    }
  }

  return 0;
}
